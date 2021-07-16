from django.urls import path

from . import views
from .views import AuthorDetailView, AuthorListView, BookDetailView, BookListView

app_name = 'rediscache'
urlpatterns = [
    path('', views.index, name='index'),
    path('author/', AuthorListView.as_view(), name='author'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('book/', BookListView.as_view(), name='book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
