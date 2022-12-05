from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView
from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackView(FormView):
    template_name = 'feedback/feedback.html'
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback:feedback')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = FeedbackForm
        return context

    def post(self, request, *args, **kwargs):

        form = FeedbackForm(request.POST or None)

        if form.is_valid():
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
            return redirect(self.get_success_url())

        return render(request, self.template_name, self.get_context_data())


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
