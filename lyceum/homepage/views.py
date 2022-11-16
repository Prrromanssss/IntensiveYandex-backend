import random

from catalog.models import Item
from django.shortcuts import render


def home(request):
    template_name = 'homepage/index.html'
    items = Item.objects.published().filter(is_on_main=True).order_by('name')
    context = {
        'items': items,
    }
    return render(request, template_name, context)
