from rest_framework import serializers
from .models import Post, Comment
from userapp.models import CustomUser
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = TagListSerializerField()
    image = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['image', 'title', 'text', 'published_date', 'author', 'tags', 'like_count', 'is_liked']
    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None
    def get_like_count(self, obj):
        return obj.liked_by.count()

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj.liked_by.filter(id=user.id).exists()
        return False
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ['post', 'text', 'created_at', 'author']