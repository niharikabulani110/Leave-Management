from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_manager')
    managed_users = models.ManyToManyField(User, related_name='managing_manager', blank=True)

    def __str__(self):
        return f"Manager: {self.user.username}"
