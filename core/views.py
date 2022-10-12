from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from . import serializers
from . import models


class TagViewSet(ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

