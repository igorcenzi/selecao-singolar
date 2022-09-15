from dataclasses import fields
from rest_framework import serializers
from .models import Likes

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"
        read_only_fields = ["id", "user", "created_at", "updated_at"]
        
    def create(self, validated_data):
        like = Likes.objects.get_or_create(**validated_data)[0]
        return like