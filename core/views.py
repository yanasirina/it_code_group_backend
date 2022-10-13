import django_filters
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from . import serializers
from . import models
from . import filters


class TagViewSet(ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = filters.Tag

