from django.shortcuts import render
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'app/home.html', context)


class BookListView(ListView):
    model = Book
    template_name = 'app/home.html'
    context_object_name = 'books'
    ordering = ['-date_added']


class BookDetailView(DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.owner:
            return True
        return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.owner:
            return True
        else:
            return False




def about(request):
    return render(request, 'app/about.html', {'title':'About'})
