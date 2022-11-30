from django.shortcuts import get_object_or_404, render

from .models import Item


def item_list(request):
    template_name = 'catalog/item_list.html'
    items = Item.objects.published().order_by('category__name', 'name')
    context = {
        'items': items,
    }
    return render(request, template_name, context)


def item_detail(request, pk):
    template_name = 'catalog/view_element.html'
    item = get_object_or_404(
        Item.objects.published(),
        pk=pk
    )
    context = {
        'item': item,
    }
    return render(request, template_name, context)
