from atexit import register
from django.contrib import admin
from CVGenProjects.models import UserProject

# Register your models here.

admin.site.register(UserProject)
