from django.db import models
import uuid

# Create your models here.
class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=140)
    post_image = models.ImageField(upload_to="post_images", blank=True, null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)