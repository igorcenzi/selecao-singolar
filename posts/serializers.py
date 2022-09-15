from rest_framework import serializers
from .models import Posts
from comments.models import Comments


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
      
      
class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        exclude = ['post']
class PostWithCommentsSerializer(serializers.ModelSerializer):
    comments = CommentPostSerializer(many=True, read_only=True)
    class Meta:
        model = Posts
        fields = ['id', 'content', 'post_image', 'user', 'comments', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'comments', 'created_at', 'updated_at']
        
