from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileUpdateForm, UserCreationForm, UserUpdateForm
from .models import Profile


@login_required
def profile(request):
    template_name = 'users/profile.html'
    form = UserUpdateForm(request.POST, instance=request.user)
    bd_form = ProfileUpdateForm(request.POST)
    context = {
        'form': form,
        'birthday_form': bd_form,
    }
    if (
        request.method == 'POST' and form.is_valid() and bd_form.is_valid()
    ):
        try:
            user = Profile.objects.get(user_id=request.user.id)
            user.birthday = bd_form.cleaned_data['birthday']
        except Exception:
            user = Profile.objects.create(
                user_id=request.user.id,
                birthday=bd_form.cleaned_data['birthday'],
            )
        finally:
            user.save()

        form.save()
        return redirect('users:profile')

    return render(request, template_name, context)


def sign_up(request):
    template_name = 'users/sign_up.html'
    form = UserCreationForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('users:login')

    return render(request, template_name, context)


def user_list(request):
    template_name = 'users/user_list.html'
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, template_name, context)


def user_detail(request, pk):
    template_name = 'users/user_detail.html'
    user = get_object_or_404(
        User,
        pk=pk
    )
    context = {
        'user': user,
    }
    return render(request, template_name, context)
