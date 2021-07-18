from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Avg, Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Author, Book


@cache_page(5)
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


@method_decorator(cache_page(10), name='dispatch')
class AuthorListView(ListView):
    model = Author
    paginate_by = 100

    def get_queryset(self):
        return Author.objects.annotate(num_books=Count('book'))


@method_decorator(cache_page(20), name='dispatch')
class AuthorDetailView(DetailView):
    model = Author

    def get_queryset(self):
        return Author.objects.prefetch_related('book_set').annotate(avg_rating=Avg('book__rating'))


@method_decorator(cache_page(10), name='dispatch')
class BookListView(ListView):
    model = Book
    paginate_by = 400

    def get_queryset(self):
        return Book.objects.prefetch_related('authors').annotate(avg_age=Avg('authors__age'))


@method_decorator(cache_page(20), name='dispatch')
class BookDetailView(DetailView):
    model = Book

    def get_queryset(self):
        return Book.objects.prefetch_related('authors').annotate(avg_age=Avg('authors__age'))


@method_decorator(cache_page(60), name='dispatch')
class AuthorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Author
    fields = ['name', 'age']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('rediscache:author')
    login_url = '/admin/'
    success_message = 'Author was created successfully'


@method_decorator(cache_page(20), name='dispatch')
class AuthorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Author
    fields = ['name', 'age']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('rediscache:author')
    login_url = '/admin/'
    success_message = 'Author was updated successfully'


@method_decorator(cache_page(20), name='dispatch')
class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('rediscache:author')
    login_url = '/admin/'


@method_decorator(cache_page(60), name='dispatch')
class BookCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Book
    fields = ['name', 'pages', 'price', 'rating', 'pubdate', 'authors']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('rediscache:book')
    login_url = '/admin/'
    success_message = 'Book was created successfully'


@method_decorator(cache_page(20), name='dispatch')
class BookUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Book
    fields = ['name', 'pages', 'price', 'rating', 'pubdate', 'authors']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('rediscache:book')
    login_url = '/admin/'
    success_message = 'Book was updated successfully'


@method_decorator(cache_page(20), name='dispatch')
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('rediscache:book')
    login_url = '/admin/'
