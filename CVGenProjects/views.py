from multiprocessing import context
from django.http import Http404
from django.shortcuts import redirect, render
from CVGenProjects.models import UserProject
from CVGenBasicInfo.models import UserBasicInfo
from django.contrib.auth.models import User
# Create your views here.


def user_projects(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    this_user_projects = UserProject.objects.filter(username=user)
    this_user_info = UserBasicInfo.objects.filter(username=user).first()

    if request.method == "POST":
        name = request.POST.get('project-name')
        image = request.FILES['project-image']
        link = request.POST.get('project-link')
        description = request.POST.get('project-description')

        UserProject.objects.create(
            username=user,
            title=name,
            image=image,
            link=link,
            description=description
        )

    context = {
        'user_projects': this_user_projects,
        "fullname": this_user_info.firstname + " " + this_user_info.lastname
    }
    return render(request, 'userpanel/projects.html', context)


def delete_this_project(request, id):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    try:
        this_skill = UserProject.objects.get(id=id, username=user)
        this_skill.delete()
    except:
        raise Http404()

    return redirect("/userpanel/user-projects")
