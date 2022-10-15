import django_filters
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from . import serializers
from . import models
from . import filters


class TagViewSet(ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = filters.Tag

    # def list(self, request, *args, **kwargs):
    #     serializer = serializers.TagSearch(data=request.query_params)
    #     serializer.is_valid(raise_exception=True)
    #
    #     return super().list(request, *args, **kwargs)


class ItemViewSet(ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    serializer_class = serializers.ItemSerializer
    filterset_class = filters.Item

    def get_queryset(self):
        return models.Item.objects.filter(user=self.request.user)


class RegisterUser(GenericAPIView):
    queryset = models.User

    def post(self, request):
        # homework
        pass
