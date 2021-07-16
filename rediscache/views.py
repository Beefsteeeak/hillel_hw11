from django.contrib.auth.mixins import LoginRequiredMixin  # noqa:F401
from django.contrib.messages.views import SuccessMessageMixin  # noqa:F401
from django.db.models import Avg, Count
from django.shortcuts import render
from django.urls import reverse_lazy  # noqa:F401
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView  # noqa:F401
from django.views.generic.list import ListView

from .models import Author, Book


def index(request):
    num_authors = Author.objects.count()
    num_books = Book.objects.count()

    return render(
        request,
        'rediscache/index.html',
        context={
            'num_authors': num_authors,
            'num_books': num_books,
        }
    )


class AuthorListView(ListView):
    model = Author
    paginate_by = 100

    def get_queryset(self):
        return Author.objects.annotate(num_books=Count('book'))


class AuthorDetailView(DetailView):
    model = Author

    def get_queryset(self):
        return Author.objects.prefetch_related('book_set').annotate(avg_rating=Avg('book__rating'))


class BookListView(ListView):
    model = Book
    paginate_by = 400

    def get_queryset(self):
        return Book.objects.prefetch_related('authors').annotate(avg_age=Avg('authors__age'))


class BookDetailView(DetailView):
    model = Book

    def get_queryset(self):
        return Book.objects.prefetch_related('authors').annotate(avg_age=Avg('authors__age'))
