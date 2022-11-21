import os

from django.core.mail import send_mail
from django.shortcuts import redirect, render
from dotenv import load_dotenv

from .forms import FeedBackForm
from .models import FeedBack

load_dotenv()


def feedback(request):
    template_name = 'feedback/index.html'
    form = FeedBackForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        mail = form.cleaned_data['mail']
        send_mail(
            text.split()[:3],
            text,
            os.environ.get('ADMIN_EMAIL', 'admin@example.com'),
            [mail],
            fail_silently=False,
        )

        feedback = FeedBack.objects.create(
            **form.cleaned_data
        )
        feedback.save()

        return redirect('feedback:feedback')

    return render(request, template_name, context)
