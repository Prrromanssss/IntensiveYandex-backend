from django.views.generic import TemplateView


class DescriptionView(TemplateView):
    template_name = 'about/about.html'

    # def get_queryset(self):
    #     return
