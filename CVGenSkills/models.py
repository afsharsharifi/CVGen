from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserSkill(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    percentage = models.IntegerField()

    def __str__(self):
        return self.username
