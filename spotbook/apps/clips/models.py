from django.db import models
from django.conf import settings
from spotbook.apps.spots.models import Spot

User = settings.AUTH_USER_MODEL

class ClipLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clip = models.ForeignKey("Clip", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Clip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    textContent = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='clip-images/')
    likes = models.ManyToManyField(User, related_name="clip_user", blank=True, through=ClipLike)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.spot.title
