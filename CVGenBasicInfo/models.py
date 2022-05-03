import os
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path_profiles(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"profile {instance.username}-{instance.birthyear}{ext}"
    return f"user_images/profiles/{final_name}"


TEMPLATE_CHOICES = (
    ('1', 'Creative CV'),
    ('2', 'I’mRex'),
    ('3', 'Material CV'),
    ('4', 'Material Resume'),
    ('5', 'Right Resume'),
)


class UserBasicInfo(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    position = models.CharField(max_length=150)
    birthyear = models.CharField(max_length=4)
    email = models.EmailField()
    mobile = models.CharField(max_length=11)
    city = models.CharField(max_length=200)
    template = models.CharField(max_length=40, choices=TEMPLATE_CHOICES, default='1')
    about = models.TextField()
    profile_image = models.ImageField(upload_to=upload_image_path_profiles, null=True, blank=True)

    # Social Media
    instagram = models.CharField(max_length=400, default="")
    telegram = models.CharField(max_length=400, default="")
    whatsapp = models.CharField(max_length=400, default="")
    github = models.CharField(max_length=400, default="")
    gitlab = models.CharField(max_length=400, default="")
    stackoverflow = models.CharField(max_length=400, default="")

    def __str__(self):
        return f"{self.username}"
