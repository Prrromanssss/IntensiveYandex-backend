from django.contrib.auth.admin import User
from django.shortcuts import render


def profile(request):
    template_name = 'users/profile.html'
    return render(request, template_name)


def sign_up(request):
    template_name = 'users/sign_up.html'
    return render(request, template_name)


def user_list(request):
    template_name = 'users/user_list.html'
    return render(request, template_name)


def user_detail(request):
    template_name = 'users/user_detail.html'
    return render(request, template_name)
