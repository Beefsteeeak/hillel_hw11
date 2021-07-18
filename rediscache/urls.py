from django.urls import path

from . import views
from .views import AuthorCreateView, AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorUpdateView,\
    BookCreateView, BookDeleteView, BookDetailView, BookListView, BookUpdateView

app_name = 'rediscache'
urlpatterns = [
    path('', views.index, name='index'),

    path('author/', AuthorListView.as_view(), name='author'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('author/create/', AuthorCreateView.as_view(), name='author-create'),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author-delete'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),

    path('book/', BookListView.as_view(), name='book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/create/', BookCreateView.as_view(), name='book-create'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
]
