from rest_framework import serializers
from .models import Post, Comment
from userapp.models import CustomUser
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = TagListSerializerField()
    class Meta:
        model = Post
        fields = ['image', 'title', 'text', 'published_date', 'author', 'tags']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ['post', 'text', 'created_at', 'author']