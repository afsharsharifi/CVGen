from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserExperience(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    logo = models.ImageField()
    isWork = models.BooleanField()
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)
