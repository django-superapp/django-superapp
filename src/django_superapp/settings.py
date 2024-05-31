import importlib
import logging
import pkgutil

from django.urls import reverse_lazy
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


def extend_superapp_settings(main_settings, package):
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        submodule_name = f"{package.__name__}.{modname}.settings"

        try:
            settings_module = importlib.import_module(submodule_name)
        except ModuleNotFoundError as e:
            if f"No module named '{submodule_name}'" in str(e):
                continue
            raise e

        if hasattr(settings_module, "extend_superapp_settings"):
            settings_module.extend_superapp_settings(main_settings)


def extend_with_superapp_settings(main_settings, superapp_apps):
    main_settings.update({
        'LOGIN_URL': "admin:login",
        'LOGIN_REDIRECT_URL': reverse_lazy("admin:index"),
    })
    main_settings['INSTALLED_APPS'] = [
                                          'admin_confirm',
                                          'unfold',
                                          "unfold.contrib.filters",
                                          "unfold.contrib.import_export",
                                          "unfold.contrib.guardian",
                                          "unfold.contrib.simple_history",
                                          "unfold.contrib.forms",
                                      ] + main_settings['INSTALLED_APPS']

    main_settings['UNFOLD'] = {
        "SITE_HEADER": _("SuperApp Demo"),
        "SITE_TITLE": _("SuperApp Demo"),
        "SITE_SYMBOL": "settings",
        "SHOW_HISTORY": False,
        "STYLES": [],
        "SCRIPTS": [
            lambda request: static("js/apex.min.js"),
            lambda request: static("js/flowbite.min.js"),
            lambda request: static("js/jquery-3.7.1.min.js"),
            lambda request: static("js/modals.js"),
        ],
    }

    extend_superapp_settings(main_settings, superapp_apps)
