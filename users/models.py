from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .utils import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ["full_name", "password"]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()