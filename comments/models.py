from django.db import models
import uuid

# Create your models here.
class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.CharField(max_length=140)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey("posts.Posts", on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)