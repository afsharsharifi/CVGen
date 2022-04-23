from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProject(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField()
    link = models.CharField(max_length=300)
    description = models.TextField()
