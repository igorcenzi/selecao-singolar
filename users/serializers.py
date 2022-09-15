from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password', 'profile_picture', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        password = False
        if "is_admin" in validated_data:
            raise ValidationError({"detail": "Can't edit field is_admin"})
        if validated_data.get("password"):
            password = validated_data.pop("password")
        if "email" in validated_data:
            raise ValidationError({"detail": "Can't edit field email"})
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance