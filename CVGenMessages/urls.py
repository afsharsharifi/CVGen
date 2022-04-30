from django.urls import path
from CVGenMessages.views import user_messages

urlpatterns = [
    path('user-messages', user_messages),
]
