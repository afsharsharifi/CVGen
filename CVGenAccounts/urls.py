from django.urls import path
from CVGenAccounts.views import user_login, user_signup

urlpatterns = [
    path('login', user_login),
    path('signup', user_signup),
]
