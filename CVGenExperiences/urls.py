from django.urls import path
from CVGenExperiences.views import user_experiences

urlpatterns = [
    path('user-experiences', user_experiences),
]
