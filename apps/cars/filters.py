from .models import CarModel

from django_filters import rest_framework as new_filter


class CarFilter(new_filter.FilterSet):
    price_gt = new_filter.NumberFilter(field_name='price', lookup_expr='gt')
    price_gte = new_filter.NumberFilter(field_name='price', lookup_expr='gte')
    price_lt = new_filter.NumberFilter(field_name='price', lookup_expr='lt')
    mark_start = new_filter.CharFilter(field_name='mark', lookup_expr='istartswith')
    mark_end = new_filter.CharFilter(field_name='mark', lookup_expr='iendswith')
    mark_in = new_filter.CharFilter(field_name='mark', lookup_expr='in')

    class Meta:
        model = CarModel
        fields = (
            'price_gt',
            'price_gte',
            'price_lt',
            'mark_start',
            'mark_end',
            'mark_in'
        )
