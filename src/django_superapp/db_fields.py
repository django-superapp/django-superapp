from django.db.models import ForeignKey


class ChainedForeignKey(ForeignKey):
    def __init__(self, *args, **kwargs):
        self.filters = kwargs.pop('filters', {})
        self.dynamic_filters = kwargs.pop('dynamic_filters', True)
        self.automatically_select_unique_choice = kwargs.pop('automatically_select_unique_choice', False)
        super().__init__(*args, **kwargs)
