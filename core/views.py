from rest_framework.viewsets import ReadOnlyModelViewSet

from . import serializers, models


class TagViewSet(ReadOnlyModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

