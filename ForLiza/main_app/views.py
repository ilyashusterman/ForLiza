from django.shortcuts import render

from .models import travels


def home(request):
    home_context = {
        'travel': ['Sweden', 'England'],
        'travels': travels
    }
    return render(request, 'home.html', context=home_context)
