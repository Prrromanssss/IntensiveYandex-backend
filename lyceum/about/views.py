from django.shortcuts import render


def description(request):
    template_name = 'about/index.html'
    return render(request, template_name)
