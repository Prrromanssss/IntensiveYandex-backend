from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'users/profile.html'
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['form'] = CustomUserChangeForm
        context['user'] = get_object_or_404(
            CustomUser,
            id=self.request.user.id,
        )

        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            form = CustomUserChangeForm(self.request.POST or None,
                                        instance=self.request.user)
            CustomUser.objects.filter(id=request.user.id).update(
                **form.cleaned_data,
            )
            form.save()
            return redirect(self.get_success_url())
        else:
            form = CustomUserChangeForm()


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


class UsersView(ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserView(DetailView):

    model = CustomUser
    template_name = 'users/user_detail.html'
    context_object_name = 'user'

    def get_queryset(self):
        return CustomUser.objects.filter(pk=self.kwargs['pk'])
