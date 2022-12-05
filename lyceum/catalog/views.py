from catalog.models import Item
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from rating.models import Rating
from users.models import CustomUser


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
        return Item.objects.published()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['grade'] = Rating.objects.filter(
            user_id=self.request.user.id,
            item_id=self.kwargs['pk']
        )
        context['number'] = Rating.objects.filter(
            item_id=self.kwargs['pk']
        ).count()
        context['user'] = get_object_or_404(
            CustomUser,
            id=self.request.user.id,
        )

        return context
