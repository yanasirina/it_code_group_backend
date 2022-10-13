import django_filters.rest_framework as filters

from . import models


class Tag(filters.FilterSet):
    min_id = filters.NumberFilter(field_name="id", lookup_expr='gte')
    max_id = filters.NumberFilter(field_name="id", lookup_expr='lte')
    id = filters.NumberFilter(field_name='id')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        models = models.Tag
        fields = '__all__'

