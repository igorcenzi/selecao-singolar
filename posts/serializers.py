from dataclasses import fields
from rest_framework import serializers
from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']