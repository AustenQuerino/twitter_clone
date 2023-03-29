from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=60) # max_length = required
    name = models.CharField(max_length=20)
    bio = models.TextField(default='Unknown')
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='default_profile_picture.png')

    def get_absolute_url(self):
        return reverse("profiles:profile-detail", kwargs={"id": self.id})

