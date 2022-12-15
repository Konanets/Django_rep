from .models import AutoParksModel

from django_filters import rest_framework as new_filter


class AutoParkFilter(new_filter.FilterSet):
    cars_year_lt = new_filter.NumberFilter(field_name='cars', lookup_expr='lt')

    class Meta:
        model = AutoParksModel
        fields = ('cars_year_lt',)
