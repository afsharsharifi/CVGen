from django.urls import path
from CVGenBasicInfo.views import user_basic_info

urlpatterns = [
    path('user-basic-info', user_basic_info),
]
