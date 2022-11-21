from django import forms

from .models import FeedBack


class FeedBackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = FeedBack
        fields = (
            FeedBack.text.field.name,
            FeedBack.mail.field.name,
            FeedBack.name.field.name,
        )
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 5,
            })
        }
