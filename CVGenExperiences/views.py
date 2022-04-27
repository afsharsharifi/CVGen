from multiprocessing import context
from django.shortcuts import render
from CVGenExperiences.models import UserExperience

from django.contrib.auth.models import User

# Create your views here.


def user_experiences(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    this_user_experiences = UserExperience.objects.filter(username=user)

    if request.method == "POST":
        name = request.POST.get('place-name')
        logo = request.POST.get('place-logo')
        isWork = True if request.POST.get('exp-position') == "yes" else False
        start = request.POST.get('start-date')
        end = request.POST.get('end-date')

    context = {}

    return render(request, 'userpanel/experiences.html', context)
