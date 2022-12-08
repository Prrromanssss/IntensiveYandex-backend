from catalog.models import Item
from django.db.models import Avg
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from rating.forms import RatingForm
from rating.models import Rating


class ItemListView(ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.published().order_by('category__name', 'name')


class ItemDetailView(FormMixin, DetailView):
    model = Item
    form_model = Rating
    template_name = 'catalog/view_element.html'
    context_object_name = 'item'
    form_class = RatingForm
    get_queryset = Item.objects.published

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.form_class(self.request.POST or None)

        context['grade'] = self.form_model.objects.filter(
            user_id=self.request.user.id,
            item_id=self.kwargs['pk'],
        )
        context['number'] = self.form_model.objects.filter(
            item_id=self.kwargs['pk'],
        ).count()
        context['average'] = self.form_model.objects.filter(
            item_id=self.kwargs['pk'],
        ).aggregate(
            Avg('grade')
        )['grade__avg']

        return context

    def get_success_url(self, **kwargs):
        if kwargs is not None:
            return reverse_lazy(
                'catalog:item_detail',
                kwargs={'pk': kwargs['pk']}
            )
        return reverse_lazy('catalog:item_detail')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            self.form_model.objects.update_or_create(
                user_id=request.user.id,
                item_id=self.kwargs['pk'],
                defaults=form.cleaned_data,
            )

            return redirect(self.get_success_url(**self.kwargs))
        return render(request, self.template_name, self.get_context_data())
