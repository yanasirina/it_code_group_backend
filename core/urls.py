from django.urls import path
from rest_framework.routers import DefaultRouter

import core.views


urlpatterns = [
    path('user/register/', core.views.RegisterUser.as_view(), name='user_register'),
    path('user/login/', core.views.LoginUser.as_view(),  name='user_login'),
]


router = DefaultRouter()
router.register('tags', core.views.TagViewSet, basename='tag')
router.register('items', core.views.ItemViewSet, basename='item')
urlpatterns += router.urls

