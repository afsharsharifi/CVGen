from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.username}-{instance.title}{ext}"
    return f"projects/{final_name}"


class UserProject(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    link = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return f"{self.username}"
