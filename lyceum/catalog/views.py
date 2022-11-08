from django.shortcuts import render

from .models import Item


def item_list(request):
    template_name = 'catalog/index.html'
    return render(request, template_name)


def item_detail(request, pk):
    template_name = 'catalog/view_element.html'
    context = {'pk': pk}
    return render(request, template_name, context)
