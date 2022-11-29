from django.shortcuts import redirect, render

from .forms import UserCreationForm


def profile(request):
    template_name = 'users/profile.html'
    return render(request, template_name)


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
    return render(request, template_name)


def user_detail(request):
    template_name = 'users/user_detail.html'
    return render(request, template_name)
