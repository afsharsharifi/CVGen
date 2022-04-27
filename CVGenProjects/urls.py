from django.urls import path
from CVGenProjects.views import user_projects

urlpatterns = [
    path('user-projects', user_projects),
]
