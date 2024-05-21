import copy
from typing import List, Optional, Dict, Any

from django.contrib.admin import helpers
from django.contrib.admin.utils import lookup_field
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models import ForeignKey
from django.forms import ModelChoiceField
from django.http import HttpRequest
from django.urls import reverse, URLPattern, path
from django.utils.text import wrap
from django_svelte_jsoneditor.widgets import SvelteJSONEditorWidget
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin, UnfoldAdminReadonlyField
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.dataclasses import UnfoldAction
from unfold.widgets import UnfoldBooleanSwitchWidget, UnfoldAdminFileFieldWidget
from django.db import models

from admin_confirm import AdminConfirmMixin

from django_superapp.db_fields import ChainedForeignKey
from django_superapp.widgets import ChainedAdminSelect


class SuperAppAdminReadonlyField(UnfoldAdminReadonlyField):

    def is_custom_html_field(self) -> bool:
        field, obj, model_admin = (
            self.field["field"],
            self.form.instance,
            self.model_admin,
        )

        try:
            f, attr, value = lookup_field(field, obj, model_admin)
        except (AttributeError, ValueError, ObjectDoesNotExist):
            return False

        return hasattr(attr, 'custom_html_field') and attr.custom_html_field == True


helpers.AdminReadonlyField = SuperAppAdminReadonlyField

class ChainedForeignKeyAdmin:
    def formfield_for_foreignkey(
            self, db_field: ForeignKey, request: HttpRequest, **kwargs
    ) -> Optional[ModelChoiceField]:
        db = kwargs.get("using")

        if isinstance(db_field, ChainedForeignKey):
            kwargs["widget"] = ChainedAdminSelect(
                db_field, self.admin_site, using=db
            )
            pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SuperAppModelAdmin(AdminConfirmMixin, ModelAdmin, ImportExportModelAdmin):
    actions_hidden = ()
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        models.JSONField: {
            "widget": SvelteJSONEditorWidget,
        },
        models.FileField: {
            "widget": UnfoldAdminFileFieldWidget,
        },
    }

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        custom_html_fields = [
            attr for attr in dir(self)
            if hasattr(getattr(self, attr), 'custom_html_field') and getattr(self, attr).custom_html_field == True
        ]

        return tuple(readonly_fields) + tuple(custom_html_fields)

    def get_actions_hidden(self, request: HttpRequest) -> List[UnfoldAction]:
        return self._filter_unfold_actions_by_permissions(
            request, self._get_base_actions_hidden()
        )

    def _get_base_actions_hidden(self) -> List[UnfoldAction]:
        """
        Returns all available detail actions, prior to any filtering
        """
        return [self.get_unfold_action(action) for action in self.actions_hidden or []]

    def changeform_view(
            self,
            request: HttpRequest,
            object_id: Optional[str] = None,
            form_url: str = "",
            extra_context: Optional[Dict[str, bool]] = None,
    ) -> Any:
        if extra_context is None:
            extra_context = {}

        new_formfield_overrides = copy.deepcopy(self.formfield_overrides)
        new_formfield_overrides.update(
            {models.BooleanField: {"widget": UnfoldBooleanSwitchWidget}}
        )

        self.formfield_overrides = new_formfield_overrides

        actions = []
        if object_id:
            for action in self.get_actions_detail(request):
                actions.append(
                    {
                        "title": action.description,
                        "attrs": action.method.attrs,
                        "path": reverse(
                            f"admin:{action.action_name}", args=(object_id,)
                        ),
                    }
                )
            for action in self.get_actions_hidden(request):
                actions.append(
                    {
                        "title": action.description,
                        "attrs": action.method.attrs,
                        "path": reverse(
                            f"admin:{action.action_name}", args=(object_id,)
                        ),
                    }
                )

        extra_context.update(
            {
                "actions_submit_line": self.get_actions_submit_line(request),
                "actions_detail": actions,
            }
        )

        return super().changeform_view(request, object_id, form_url, extra_context)

    def get_urls(self) -> List[URLPattern]:
        urls = super().get_urls()

        action_hidden_urls = [
            path(
                f"<path:object_id>/{action.path}/",
                wrap(action.method),
                name=action.action_name,
            )
            for action in self._get_base_actions_hidden()
        ]
        return urls + action_hidden_urls


class BaseModel(models.Model):
    def clean(self):
        super().clean()
        for field in self._meta.fields:
            if isinstance(field, ChainedForeignKey):
                computed_filters = {}
                if field.dynamic_filters:
                    for key, value in field.filters.items():
                        computed_filters[key] = getattr(self, value).pk or None
                else:
                    computed_filters = field.filters
                if not field.remote_field.model.objects.filter(**{
                    **computed_filters,
                    'pk': getattr(self, field.name).pk or None
                }).exists():
                    raise ValidationError(
                        {
                            field.name: ValidationError(
                                f"Invalid value for {field.name}",
                                code='invalid'
                            )
                        }
                    )

    class Meta:
        abstract = True
