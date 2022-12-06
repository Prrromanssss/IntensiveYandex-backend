from django import forms
from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Feedback
        fields = (
            Feedback.text.field.name,
            Feedback.mail.field.name,
            Feedback.name.field.name,
        )
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 5,
            })
        }
