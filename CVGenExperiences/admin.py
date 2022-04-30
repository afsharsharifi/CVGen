from django.contrib import admin
from CVGenExperiences.models import UserExperience
# Register your models here.


class UserExperienceAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'start', 'end']
    search_fields = ['name', 'username']

    class Meta:
        model = UserExperience


admin.site.register(UserExperience, UserExperienceAdmin)
