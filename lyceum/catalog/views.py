from catalog.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView
from rating.forms import RatingForm
from rating.models import Rating
from users.models import CustomUser


class ItemListView(ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.published().order_by('category__name', 'name')


class ItemDetailView(DetailView):
    model = Item
    template_name = 'catalog/view_element.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Item.objects.published()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['form'] = RatingForm(self.request.POST or None)
        context['grade'] = Rating.objects.filter(
            user_id=self.request.user.id,
            item_id=self.kwargs['pk']
        )
        context['number'] = Rating.objects.filter(
            item_id=self.kwargs['pk']
        ).count()
        context['average'] = Rating.objects.filter(
            item_id=self.kwargs['pk']
        ).aggregate(
            Avg('grade')
        )['grade__avg']
        if self.request.user.is_authenticated:
            context['user'] = get_object_or_404(
                CustomUser,
                id=self.request.user.id
            )

        return context


class ItemDetailGet(DetailView):
    model = Item
    template_name = 'catalog/view_element.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Item.objects.published()


class ItemDetailPost(LoginRequiredMixin, FormView):
    model = Rating
    template_name = 'catalog/view_element.html'
    form_class = RatingForm
    success_url = reverse_lazy('catalog:item_detail')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.form_class(self.request.POST or None)
        context['grade'] = self.model.objects.filter(
            user_id=self.request.user.id,
            item_id=self.kwargs['pk']
        )
        context['number'] = self.model.objects.filter(
            item_id=self.kwargs['pk']
        ).count()
        context['average'] = self.model.objects.filter(
            item_id=self.kwargs['pk']
        ).aggregate(
            Avg('grade')
        )['grade__avg']
        if self.request.user.is_authenticated:
            context['user'] = get_object_or_404(
                self.model,
                id=self.request.user.id
            )
        return context

    def post(self, request):
        form = self.form_class(
            request.POST or None,
            instance=request.user,
        )
        if form.is_valid():
            self.model.objects.filter(id=request.user.id).update(
                **form.cleaned_data,
            )
            return redirect(self.get_success_url())
        return render(request, self.template_name, self.get_context_data())
