from django.shortcuts import render


def handle_not_found(request, exception):
    return render(request, 'status_codes/404.html')
