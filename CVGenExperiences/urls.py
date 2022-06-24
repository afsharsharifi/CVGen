from django.urls import path
from CVGenExperiences.views import user_experiences, delete_this_ex

urlpatterns = [
    path('user-experiences', user_experiences),
    path('del-ex/<int:id>', delete_this_ex),
]
