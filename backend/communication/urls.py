from django.urls import path, include
from .views import PostViewSet, CommentViewSet, toggle_like
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"post", PostViewSet)
router.register(r"comment", CommentViewSet)

urlpatterns= [
    path('', include(router.urls)),
    path('posts/<int:post_id>/toggle_like/', toggle_like, name='toggle_like'),
]