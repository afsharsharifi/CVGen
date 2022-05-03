from django.urls import path
from CVGenResumes.views import show_resume

urlpatterns = [
    path('r/<username>', show_resume),
]
