from multiprocessing import context
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from CVGenSkills.models import UserSkill
from CVGenBasicInfo.models import UserBasicInfo
# Create your views here.


def user_skills(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    this_user_skills = UserSkill.objects.filter(username=user)
    this_user_info = UserBasicInfo.objects.filter(username=user).first()
    if request.method == "POST":
        title = request.POST.get('skill-title')
        percentage = request.POST.get('skill-percentage')

        UserSkill.objects.create(
            username=user,
            title=title,
            percentage=percentage
        )
    try:
        fullname = this_user_info.firstname + " " + this_user_info.lastname
    except:
        fullname = "پنل کاربری"
    context = {
        'user_skills': this_user_skills,
        "fullname": fullname
    }
    return render(request, 'userpanel/skills.html', context)


def delete_this_skill(request, id):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    try:
        this_skill = UserSkill.objects.get(id=id, username=user)
        this_skill.delete()
    except:
        raise Http404()

    return redirect("/userpanel/user-skills")
