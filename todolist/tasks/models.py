from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth import get_user_model


# Create your models here.
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_users_groups')


class ToDo(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='todos'  # Add or change the related_name
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
