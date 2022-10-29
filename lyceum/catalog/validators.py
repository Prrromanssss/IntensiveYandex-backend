from django.core.exceptions import ValidationError


def validate_amazing(value):
    must_be_in_our_item = {'превосходно', 'роскошно'}
    cleaned_value = set(value.lower().split())

    difference = must_be_in_our_item - cleaned_value

    if len(difference) == len(must_be_in_our_item):
        raise ValidationError(f'''Обязательно нужно использовать
                             {" ".join(must_be_in_our_item)}''')

    return value


# def validate_amazing(*args):
#     def validate_with_params(value):
#         must_be_in_our_item = set(args)

#         cleaned_value = set(value.lower().split())

#         difference = must_be_in_our_item - cleaned_value

#         if len(difference) == len(must_be_in_our_item):
#             raise ValidationError(f'''Обязательно нужно использовать
#                                  {" ".join(must_be_in_our_item)}''')
#     return validate_with_params
