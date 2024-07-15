from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)\/comments', CommentViewSet, basename='comments'
)
router.register('', include('djoser.urls.jwt'))

urlpatterns = [
    path('', include(router.urls)),
]
