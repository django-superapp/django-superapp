import importlib
import logging
import pkgutil


logger = logging.getLogger(__name__)


def extend_superapp_settings(main_settings, superapp_apps):
    for importer, modname, ispkg in pkgutil.iter_modules(superapp_apps.__path__):
        submodule_name = f"{superapp_apps.__name__}.{modname}.settings"

        try:
            settings_module = importlib.import_module(submodule_name)
        except ModuleNotFoundError as e:
            if f"No module named '{submodule_name}'" in str(e):
                continue
            raise e

        if hasattr(settings_module, "extend_superapp_settings"):
            settings_module.extend_superapp_settings(main_settings)
