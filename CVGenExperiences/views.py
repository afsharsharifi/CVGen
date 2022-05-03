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
        logo = request.FILES['place-logo']
        isWork = True if request.POST.get('exp-position') == "yes" else False
        start = request.POST.get('start-date')
        end = request.POST.get('end-date')

        UserExperience.objects.create(
            username=user,
            name=name,
            logo=logo,
            isWork=isWork,
            start=start,
            end=end,
        )

    context = {
        'user_experiences': this_user_experiences
    }

    return render(request, 'userpanel/experiences.html', context)
