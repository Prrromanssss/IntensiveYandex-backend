import os

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import FeedbackForm
from .models import Feedback


def feedback(request):
    template_name = 'feedback/feedback.html'
    form = FeedbackForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        text = form.cleaned_data['text']
        mail = form.cleaned_data['mail']
        message = (
            f'Здравствуйте, {name}! '
            'Вы получили это письмо, так как написали в Boyko Company.\n'
            f'Ваш отзыв:\n{text}\n\n'
            'Спасибо за фидбэк! Мы обязательно учтем ваше мнение.\n'
            '© Boyko Company'
        )

        send_mail(
            'Boyko company',
            message,
            settings.ADMIN_EMAIL,
            [mail],
            fail_silently=False,
        )

        Feedback.objects.create(
            **form.cleaned_data
        )

        return redirect('feedback:feedback')

    return render(request, template_name, context)
