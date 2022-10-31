from functools import wraps

from django.core.exceptions import ValidationError


def validate_amazing(*args):
    @wraps(validate_amazing)
    def validator(value):
        must_words = args

        if not any(filter(lambda word: word.lower() in value.lower(),
                   must_words)):
            raise ValidationError(
                f'Обязательно нужно использовать'
                f' {" ".join(must_words)}'
            )
        return value

    return validator
