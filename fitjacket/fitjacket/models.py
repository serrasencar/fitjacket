from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skill_level = models.CharField(max_length=20)
    goals = models.JSONField(blank=True, null=True)  #

    def __str__(self):
        return self.user.username

