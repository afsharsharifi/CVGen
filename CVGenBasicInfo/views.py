from django.shortcuts import render
from jdatetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from CVGenBasicInfo.models import UserBasicInfo

# Create your views here.


@login_required(login_url='/login')
def user_basic_info(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    this_user_info = UserBasicInfo.objects.filter(username=user).first()
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        position = request.POST.get('position')
        birthyear = request.POST.get('birthyear')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        template = request.POST.get('select-template')
        about = request.POST.get('about')

        if this_user_info:
            this_user_info.firstname = firstname
            this_user_info.lastname = lastname
            this_user_info.position = position
            this_user_info.birthyear = birthyear
            this_user_info.email = email
            this_user_info.mobile = phone
            this_user_info.city = city
            this_user_info.template = template
            this_user_info.about = about
            this_user_info.save()
        else:
            UserBasicInfo.objects.create(
                username=user,
                firstname=firstname,
                lastname=lastname,
                position=position,
                birthyear=birthyear,
                email=email,
                mobile=phone,
                city=city,
                template=template,
                about=about
            )

    context = {
        'user_info': this_user_info
    }

    return render(request, 'userpanel/basic-info.html', context)
