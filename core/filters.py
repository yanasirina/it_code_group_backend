import django_filters

from . import models


class Tag(django_filters.rest_framework.FilterSet):
    # id = django_filters.NumberFilter(field_name='id', lookup_expr='gte')
    id = django_filters.NumberFilter(field_name='id')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        models = models.Tag
        fields = '__all__'

