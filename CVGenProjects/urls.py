from django.urls import path
from CVGenProjects.views import user_projects, delete_this_project

urlpatterns = [
    path('user-projects', user_projects),
    path('del-project/<int:id>', delete_this_project),
]
