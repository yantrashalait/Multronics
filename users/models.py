from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_pics')
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username + ' - ' + 'Profile'
