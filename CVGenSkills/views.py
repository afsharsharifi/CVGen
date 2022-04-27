from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.models import User
from CVGenSkills.models import UserSkill
# Create your views here.


def user_skills(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    this_user_skills = UserSkill.objects.filter(username=user)
    if request.method == "POST":
        title = request.POST.get('skill-title')
        percentage = request.POST.get('skill-percentage')

        UserSkill.objects.create(
            username=user,
            title=title,
            percentage=percentage
        )

    context = {
        'user_skills': this_user_skills
    }
    return render(request, 'userpanel/skills.html', context)
