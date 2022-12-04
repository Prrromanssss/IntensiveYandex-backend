from catalog.models import Item
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView


class ItemsView(ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.published().order_by('category__name', 'name')


class ItemView(DetailView):

    model = Item
    template_name = 'catalog/view_element.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Item.objects.published().filter(pk=self.kwargs['pk'])
