from django.shortcuts import render
from .models import Book



def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'app/home.html', context)


def about(request):
    return render(request, 'app/about.html', {'title':'About'})
