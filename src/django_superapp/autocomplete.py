import json

from django.contrib.admin.views.autocomplete import AutocompleteJsonView


class SmartSelectAutocompleteJsonView(AutocompleteJsonView):
    def get_queryset(self):
        """Return queryset based on ModelAdmin.get_search_results()."""
        qs = self.model_admin.get_queryset(self.request)
        qs = qs.complex_filter(self.source_field.get_limit_choices_to())
        qs, search_use_distinct = self.model_admin.get_search_results(
            self.request, qs, self.term
        )
        filters = json.loads(self.request.GET.get('filters', '{}'))

        qs = qs.filter(**filters)

        if search_use_distinct:
            qs = qs.distinct()
        return qs
