from django.shortcuts import render

from .models import Travel


def home(request):
    home_context = {
        'travel': ['Sweden', 'England'],
        'travels': Travel.objects.all()
    }
    return render(request, 'home.html', context=home_context)
