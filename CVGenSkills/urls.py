from django.urls import path
from CVGenSkills.views import user_skills, delete_this_skill

urlpatterns = [
    path('user-skills', user_skills),
    path('del-skills/<int:id>', delete_this_skill),
]
