from django.shortcuts import render

from CVGenMessages.models import UserMessage
from CVGenBasicInfo.models import UserBasicInfo
from django.contrib.auth.models import User
# Create your views here.


# def header(request, *args, **kwargs):
#     context = {}
#     return render(request, 'index/shared/Header.html', context)


# def footer(request, *args, **kwargs):
#     context = {}
#     return render(request, 'index/shared/Footer.html', context)


def index(request):
    # if request.method == "POST":
    #     fullname = request.POST.get('fullname')
    #     title = request.POST.get('title')
    #     message = request.POST.get('message')

    #     UserMessage.objects.create(
    #         username=User.objects.first(),
    #         fullname=fullname,
    #         title=title,
    #         message=message
    #     )
    context = {
        "number_of_users": User.objects.all().count(),
        "number_of_resumes": UserBasicInfo.objects.all().count(),
    }
    return render(request, "index.html", context)
