from django.contrib import admin
from CVGenSkills.models import UserSkill
# Register your models here.


class UserSkillAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'percentage']
    search_fields = ['username', 'title']

    class Meta:
        model = UserSkill


admin.site.register(UserSkill, UserSkillAdmin)
