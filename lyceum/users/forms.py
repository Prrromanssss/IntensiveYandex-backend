from django import forms
from django.contrib.auth.admin import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

from .models import Profile


class UserCreationForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
        self.fields.pop('password')

    class Meta:
        model = User
        fields = ('email', 'first_name')
        exclude = ('username',)


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
        self.fields['birthday'].required = False

    class Meta:
        model = Profile
        fields = ('birthday',)
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
