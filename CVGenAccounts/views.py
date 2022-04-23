from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from CVGenAccounts.forms import LoginForm, SignupForm

# Create your views here.


def user_signup(request):
    # if request.user.is_authenticated:
    #     return redirect('/')

    signup_form = SignupForm(request.POST or None)
    if signup_form.is_valid():
        username = signup_form.cleaned_data.get('username')
        email = signup_form.cleaned_data.get('email')
        password = signup_form.cleaned_data.get('password')

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/login')
    context = {
        'signup_form': signup_form
    }

    return render(request, 'accounts/signup.html', context)


def user_login(request):
    # if request.user.is_authenticated:
    #     return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            login_form.add_error('username', 'کاربری با این مشخصات یافت نشد!')
    context = {
        'login_form': login_form
    }

    return render(request, 'accounts/login.html', context)
