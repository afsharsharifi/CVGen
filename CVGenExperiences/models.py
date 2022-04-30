import os
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.username}-{instance.name}{ext}"
    return f"experiences/{final_name}"


class UserExperience(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    isWork = models.BooleanField()
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.username}"
