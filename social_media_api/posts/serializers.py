from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

### Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Shows author's username
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), required=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']

    def create(self, validated_data):
        # Automatically assign the author from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user
        return super().create(validated_data)

### Post Serializer
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Shows author's username
    comments = CommentSerializer(many=True, read_only=True)  # Nested comments

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'comments', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']

    def create(self, validated_data):
        # Automatically assign the author from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user
        return super().create(validated_data)
