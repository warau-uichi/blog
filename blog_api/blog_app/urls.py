from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import (
    CreateUserView,
    BlogListView,
    BlogRetrieveView,
    BlogViewSet,
    NewsListView,
    NewsRetrieveView,
    NewsViewSet,
)


router = routers.DefaultRouter()
router.register('blog', BlogViewSet, basename='blog')
router.register('news', NewsViewSet, basename='news')

urlpatterns = [
    path('list-blog/', BlogListView.as_view(), name='list-blog'),
    path('detail-blog/<str:pk>/', BlogRetrieveView.as_view(), name='detail-blog'),
    path('list-news/', NewsListView.as_view(), name='list-news'),
    path('detail-news/<str:pk>/', NewsRetrieveView.as_view(), name='detail-news'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]