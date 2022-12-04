from catalog.models import Item
from django.shortcuts import render
from django.views.generic import ListView


class HomeView(ListView):
    model = Item
    template_name = 'homepage/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.published().filter(is_on_main=True)


# def home(request):
#     template_name = 'homepage/index.html'
#     items = Item.objects.published().filter(is_on_main=True)
#     context = {
#         'items': items,
#     }
#     return render(request, template_name, context)
