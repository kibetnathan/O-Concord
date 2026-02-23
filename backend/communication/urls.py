from django.urls import path, include
from .views import PostViewSet, CommentViewSet, posts, create_post
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"post", PostViewSet)
router.register(r"comment", CommentViewSet)

urlpatterns= [
    path('api/', include(router.urls)),
    path('posts/', posts, name='posts'),
    path("posts/create/", create_post, name="create_post"),
]