from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = 'Truncate all models of a specified app'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='Name of the Django app')

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']
        app_models = apps.get_app_config(app_name).get_models()

        for model in app_models:
            model.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('All models truncated successfully.'))
