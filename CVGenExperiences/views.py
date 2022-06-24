from django.http import Http404
from django.shortcuts import redirect, render

from CVGenExperiences.models import UserExperience
from CVGenBasicInfo.models import UserBasicInfo

from django.contrib.auth.models import User

# Create your views here.


def user_experiences(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    this_user_experiences = UserExperience.objects.filter(username=user)
    this_user_info = UserBasicInfo.objects.filter(username=user).first()

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
    try:
        fullname = this_user_info.firstname + " " + this_user_info.lastname
    except:
        fullname = "پنل کاربری"
    context = {
        'user_experiences': this_user_experiences,
        "fullname": fullname
    }

    return render(request, 'userpanel/experiences.html', context)


def delete_this_ex(request, id):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    try:
        this_skill = UserExperience.objects.get(id=id, username=user)
        this_skill.delete()
    except:
        raise Http404()

    return redirect("/userpanel/user-experiences")
