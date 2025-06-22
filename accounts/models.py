from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.png')
    rating = models.FloatField(default=5.0)

    def __str__(self):
        return f"{self.user.username} profili"