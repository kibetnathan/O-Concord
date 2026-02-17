from django.urls import path, include
from .views import PostViewSet, CommentViewSet, posts, posts_form
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns= [
    path('api/', include(router.urls)),
    path('posts/', posts, name='posts'),
    path('posts/new/', posts_form, name='post_form'),
]