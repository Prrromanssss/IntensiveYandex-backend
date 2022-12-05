from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView, UpdateView

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'users/profile.html'
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('users:profile')

    def post(self, request):

        form = CustomUserChangeForm(self.request.POST or None,
                                    instance=self.request.user)

        if form.is_valid():
            CustomUser.objects.filter(id=request.user.id).update(
                **form.cleaned_data,
            )
            form.save()
            return redirect(self.get_success_url())

        context = {'form': form, 'user': self.request.user}

        return render(request, self.template_name, context)


class SignUpView(FormView):
    template_name = 'users/sign_up.html'
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = CustomUserCreationForm
        return context

    def post(self, request):
        form = self.get_form()

        if form.is_valid():
            form = CustomUserCreationForm(self.request.POST or None)
            user = form.save()
            login(request, user)
            return redirect(self.get_success_url())

        return render(request, self.template_name, self.get_context_data())


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
