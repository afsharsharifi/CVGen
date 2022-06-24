from django.shortcuts import render
from django.contrib.auth.models import User
from CVGenMessages.models import UserMessage
from CVGenBasicInfo.models import UserBasicInfo
# Create your views here.


def user_messages(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    this_user_messages = UserMessage.objects.filter(username=user)
    this_user_info = UserBasicInfo.objects.filter(username=user).first()

    context = {
        'user_messages': this_user_messages,
        "fullname": this_user_info.firstname + " " + this_user_info.lastname
    }

    return render(request, 'userpanel/messages.html', context)
