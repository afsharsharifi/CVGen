from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserMessage(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    title = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.username}"
