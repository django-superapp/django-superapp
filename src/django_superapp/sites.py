from typing import Optional, Dict, Any

from django.http import HttpRequest
from django.template.response import TemplateResponse
from unfold.sites import UnfoldAdminSite

from .forms import LoginForm

from .urls import main_admin_urlpatterns


class SuperAppAdminSite(UnfoldAdminSite):
    login_form = LoginForm

    def get_urls(self):
        urlpatterns = [
                          x for x in main_admin_urlpatterns
                      ] + super().get_urls()

        return urlpatterns

    def custom_admin_page(self, view):
        def generator(request: HttpRequest, extra_context: Optional[Dict[str, Any]] = None,
                      **kwargs) -> TemplateResponse:
            app_list = self.get_app_list(request)

            context = {
                **self.each_context(request),
                "title": self.index_title,
                "subtitle": None,
                "app_list": app_list,
                "index": True,
                **(extra_context or {}),
            }

            request.current_app = self.name

            view_instance = view.as_view()
            return view_instance(request, context, **kwargs)

        return generator


superapp_admin_site = SuperAppAdminSite()
