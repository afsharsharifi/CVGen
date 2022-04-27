from django.urls import path
from CVGenSkills.views import user_skills

urlpatterns = [
    path('user-skills', user_skills),
]
