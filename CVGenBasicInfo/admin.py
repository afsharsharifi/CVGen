from pyexpat import model
from django.contrib import admin
from CVGenBasicInfo.models import UserBasicInfo
# Register your models here.


class UserBasicInfoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'firstname', 'lastname', 'birthyear', 'city']
    search_fields = ['firstname', 'lastname']

    class Meta:
        model = UserBasicInfo


admin.site.register(UserBasicInfo, UserBasicInfoAdmin)
