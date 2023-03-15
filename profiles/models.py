from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=60) # max_length = required
    name = models.CharField(max_length=20)
    bio = models.TextField(default='Unknown')
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

