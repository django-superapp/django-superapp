from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission

class Command(BaseCommand):
    help = 'List all permission names, slugs, and apps'

    def handle(self, *args, **kwargs):
        permissions = Permission.objects.all()
        self.stdout.write("Permission Name\tPermission Slug")
        for permission in permissions:
            self.stdout.write(f"{permission.name}\t{permission.content_type.app_label}.{permission.codename}")
