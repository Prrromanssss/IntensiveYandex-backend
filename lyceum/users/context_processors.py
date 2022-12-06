from datetime import date

from django.contrib.auth import get_user_model


def current_birthdays(request):
    birthdays = (get_user_model().objects.filter(
        birthday=date.today().strftime('%Y-%m-%d'))
        .only('first_name', 'email'))

    return {
        'birthdays': birthdays
    }
