from django.contrib.auth.admin import User
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm


class UserCreationForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
