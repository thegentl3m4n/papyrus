from django.urls import path
from . import views
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('about/', views.about, name='about'),

]
