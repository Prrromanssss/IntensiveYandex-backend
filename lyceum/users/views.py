from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView
from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import CustomUser


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'users/profile.html'
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('users:profile')

    def get(self, request):
        form = self.form_class(
            initial=self.initial,
            instance=request.user,
        )
        context = {'form': form, 'user': request.user}
        return render(
            request,
            self.template_name,
            context,
        )

    def post(self, request):
        form = self.form_class(
            request.POST or None,
            instance=request.user,
        )
        if form.is_valid():
            self.model.objects.filter(id=request.user.id).update(
                **form.cleaned_data,
            )
            return redirect(self.get_success_url())
        context = {'form': form, 'user': request.user}
        return render(request, self.template_name, context)


class SignUpView(FormView):
    template_name = 'users/sign_up.html'
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserListView(ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'users/user_detail.html'
    context_object_name = 'user'
