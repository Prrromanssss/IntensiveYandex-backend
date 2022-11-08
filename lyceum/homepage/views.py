from django.shortcuts import render


def home(request):
    template_name = 'homepage/index.html'
    return render(request, template_name)
