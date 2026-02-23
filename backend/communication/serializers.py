from rest_framework import serializers
from .models import Post, Comment
from userapp.models import CustomUser
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = TagListSerializerField()
    image = serializers.SerializerMethodField
    class Meta:
        model = Post
        fields = ['image', 'title', 'text', 'published_date', 'author', 'tags']
    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ['post', 'text', 'created_at', 'author']