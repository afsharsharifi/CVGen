from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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

    def __str__(self):
        return f"{self.username}"
