from django_filters import rest_framework as filters

from library.models import Tale


class TaleFilter(filters.FilterSet):
    class Meta:
        model = Tale
        fields = {
            'title': ['exact'],
            'owner__username': ['exact'],
            'genre': ['exact'],
            'min_age': ['lt', 'gt']
        }
