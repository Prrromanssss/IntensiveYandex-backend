from functools import wraps
from string import punctuation

from django.core.exceptions import ValidationError


def validate_amazing(*args):
    @wraps(validate_amazing)
    def validator(value):
        must_words = set(args)

        for sign in punctuation:
            value = value.replace(sign, ' ')

        cleaned_text = set(value.lower().split())

        difference = must_words - cleaned_text

        if len(difference) == len(must_words):
            raise ValidationError(
                f'Обязательно нужно использовать'
                f' {" ".join(must_words)}'
            )
        return value

    return validator
