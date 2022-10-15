from django.urls import path
from rest_framework.routers import DefaultRouter

import core.views

urlpatterns = []

router = DefaultRouter()
router.register('tags', core.views.TagViewSet, basename='tag')
router.register('items', core.views.ItemViewSet, basename='item')
urlpatterns += router.urls

