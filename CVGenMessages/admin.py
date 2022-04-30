from django.contrib import admin
from CVGenMessages.models import UserMessage
# Register your models here.


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'fullname', 'title', 'email']
    list_search = ['username', 'fullname', 'title', 'email']


admin.site.register(UserMessage, UserMessageAdmin)
