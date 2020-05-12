from django.shortcuts import render
from .models import post


# Create your views here.


books = [
    {
        'author': 'CoreyMS',
        'title': 'Book 1',
        'content': 'First Book content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Book 2',
        'content': 'Second book content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'books': post.object.all()
    }
    return render(request, 'app/home.html', context)


def about(request):
    return render(request, 'app/about.html', {'title':'About'})
