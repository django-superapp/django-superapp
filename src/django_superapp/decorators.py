from typing import Any, Callable, Dict, Iterable, Optional, Union

from django.contrib.admin.options import BaseModelAdmin
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse
from unfold.decorators import action
from unfold.typing import ActionFunction


def custom_html_field(
        function: Optional[Callable] = None,
        *,
        permissions: Optional[Iterable[str]] = None,
        description: Optional[str] = None,
        url_path: Optional[str] = None,
        attrs: Optional[Dict[str, Any]] = None,
) -> ActionFunction:
    action
    def decorator(func: Callable) -> ActionFunction:
        def inner(
                model_admin: BaseModelAdmin,
                request: HttpRequest,
                *args: Any,
                **kwargs,
        ) -> Optional[HttpResponse]:
            if permissions:
                permission_checks = (
                    getattr(model_admin, f"has_{permission}_permission")
                    for permission in permissions
                )
                # TODO add obj parameter into has_permission method call.
                # Permissions methods have following syntax: has_<some>_permission(self, request, obj=None):
                # But obj is not examined by default in django admin and it would also require additional
                # fetch from database, therefore it is not supported yet
                if not any(
                        has_permission(request) for has_permission in permission_checks
                ):
                    raise PermissionDenied
            return func(model_admin, request, *args, **kwargs)

        if permissions is not None:
            inner.allowed_permissions = permissions
        if description is not None:
            inner.short_description = description
        if url_path is not None:
            inner.url_path = url_path
        inner.attrs = attrs or {}
        inner.custom_html_field = True
        return inner

    if function is None:
        return decorator
    else:
        return decorator(function)

