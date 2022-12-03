from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@login_required
def profile(request):
    template_name = 'users/profile.html'
    form = CustomUserChangeForm(request.POST or None, instance=request.user)
    user = get_object_or_404(
        CustomUser,
        id=request.user.id,
    )
    context = {
        'form': form,
        'user': user,
    }
    if request.method == 'POST' and form.is_valid():
        CustomUser.objects.filter(id=request.user.id).update(
            **form.cleaned_data,
        )
        return redirect('users:profile')

    return render(request, template_name, context)


def sign_up(request):
    template_name = 'users/sign_up.html'
    form = CustomUserCreationForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():

        user = form.save()
        login(request, user)

        return redirect('users:profile')

    return render(request, template_name, context)


def user_list(request):
    template_name = 'users/user_list.html'
    users = CustomUser.objects.all()
    context = {
        'users': users,
    }
    return render(request, template_name, context)


def user_detail(request, pk):
    template_name = 'users/user_detail.html'
    user = get_object_or_404(
        CustomUser,
        pk=pk
    )
    context = {
        'user': user,
    }
    return render(request, template_name, context)
