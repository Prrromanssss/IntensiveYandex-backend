from functools import wraps
from string import punctuation

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateAmazing:
    def __init__(self, *words):
        self.words = words

    def __call__(self, value):
        must_words = set(self.words)
        cleaned_text = value
        for sign in punctuation:
            cleaned_text = cleaned_text.replace(sign, ' ')
        cleaned_text = set(cleaned_text.lower().split())
        difference = must_words - cleaned_text
        if len(difference) == len(must_words):
            raise ValidationError(
                f'Обязательно нужно использовать'
                f' {", ".join(must_words)}'
            )


def validate_amazing(*args):
    @wraps(validate_amazing)
    def validator(value):
        must_words = set(args)
        cleaned_text = value
        for sign in punctuation:
            cleaned_text = cleaned_text.replace(sign, ' ')
        cleaned_text = set(cleaned_text.lower().split())
        difference = must_words - cleaned_text
        if len(difference) == len(must_words):
            raise ValidationError(
                f'Обязательно нужно использовать'
                f' {" ".join(must_words)}'
            )
        return value

    return validator
