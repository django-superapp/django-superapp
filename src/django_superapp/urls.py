import importlib
import logging
import pkgutil

from django.urls import path

logger = logging.getLogger(__name__)

def extend_superapp_urlpatterns(main_urlpatterns, package):
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        submodule_name = f"{package.__name__}.{modname}.urls"

        try:
            urls_module = importlib.import_module(submodule_name)
        except ModuleNotFoundError as e:
            if f"No module named '{submodule_name}'" in str(e):
                continue
            raise e

        if hasattr(urls_module, "extend_superapp_urlpatterns"):
            urls_module.extend_superapp_urlpatterns(main_urlpatterns)


def extend_superapp_admin_urlpatterns(main_admin_urlpatterns, package):
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        submodule_name = f"{package.__name__}.{modname}.urls"

        try:
            urls_module = importlib.import_module(submodule_name)
        except ModuleNotFoundError as e:
            if f"No module named '{submodule_name}'" in str(e):
                continue
            raise e

        if hasattr(urls_module, "extend_superapp_admin_urlpatterns"):
            urls_module.extend_superapp_admin_urlpatterns(main_admin_urlpatterns)


main_admin_urlpatterns = []


def extend_with_superapp_urlpatterns(main_urlpatterns, superapp_apps):
    from django_superapp.sites import superapp_admin_site
    main_urlpatterns += [
        path("portal/", superapp_admin_site.urls),
    ]
    extend_superapp_urlpatterns(main_urlpatterns, superapp_apps)
    extend_superapp_admin_urlpatterns(main_admin_urlpatterns, superapp_apps)
