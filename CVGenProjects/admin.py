from atexit import register
from django.contrib import admin
from CVGenProjects.models import UserProject

# Register your models here.


class UserProjectAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'link']

    class Meta:
        model = UserProject


admin.site.register(UserProject, UserProjectAdmin)
