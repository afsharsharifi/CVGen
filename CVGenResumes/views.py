from multiprocessing import context
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User

from CVGenBasicInfo.models import UserBasicInfo
from CVGenExperiences.models import UserExperience
from CVGenProjects.models import UserProject
from CVGenSkills.models import UserSkill
from CVGenMessages.models import UserMessage
# Create your views here.


def show_resume(request, username):
    isUserExist = User.objects.filter(username=username).exists()
    if not isUserExist:
        raise Http404()
    user = User.objects.get(username=username)
    this_user_basicinfo = UserBasicInfo.objects.get(username=user)
    this_user_experiences = UserExperience.objects.filter(username=user)
    this_user_projects = UserProject.objects.filter(username=user)
    this_user_skills = UserSkill.objects.filter(username=user)

    if request.method == "POST":
        fullname = request.POST.get('fullname')
        title = request.POST.get('title')
        email = request.POST.get('email')
        message = request.POST.get('message')

        UserMessage.objects.create(
            username=user,
            fullname=fullname,
            title=title,
            email=email,
            message=message
        )

    context = {
        'user_baisc_info': this_user_basicinfo,
        'user_experiences': this_user_experiences,
        'user_projects': this_user_projects,
        'user_skills': this_user_skills,
    }

    choice_template = this_user_basicinfo.template

    if choice_template == '1':
        return render(request, 'resume-template/CreativeCV.html', context)
    elif choice_template == '2':
        return render(request, 'resume-template/ImRex.html', context)
    elif choice_template == '3':
        return render(request, 'resume-template/MaterialCV.html', context)
    elif choice_template == '4':
        return render(request, 'resume-template/MaterialResume.html', context)
    elif choice_template == '5':
        return render(request, 'resume-template/RightResume.html', context)
    else:
        raise Http404()
