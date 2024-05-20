from django.core.management.base import BaseCommand
from django.urls import URLResolver, URLPattern


def list_urls(urlpatterns, prefix='', depth=0):
    for pattern in urlpatterns:
        if isinstance(pattern, URLPattern):
            print(f"{'  ' * depth}{prefix}{pattern.pattern}   (name={pattern.name})")
        elif isinstance(pattern, URLResolver):
            list_urls(
                pattern.url_patterns,
                prefix + pattern.pattern.regex.pattern,
                depth + 1
            )


class Command(BaseCommand):
    help = 'List all URL patterns in the Django project'

    def handle(self, *args, **options):
        from django.urls import get_resolver
        resolver = get_resolver()
        list_urls(resolver.url_patterns)
