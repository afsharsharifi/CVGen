from multiprocessing import context
from django.shortcuts import render
from CVGenProjects.models import UserProject
from django.contrib.auth.models import User
# Create your views here.


def user_projects(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    this_user_projects = UserProject.objects.filter(username=user)

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
        'user_projects': this_user_projects
    }
    return render(request, 'userpanel/projects.html', context)
