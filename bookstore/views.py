from django.db.models import Avg, Count
from django.shortcuts import render

from .models import Author, Book, Publisher, Store


def index(request):
    num_authors = Author.objects.count()
    num_publishers = Publisher.objects.count()
    num_books = Book.objects.count()
    num_stores = Store.objects.count()

    return render(
        request,
        'bookstore/index.html',
        context={
            'num_authors': num_authors,
            'num_publishers': num_publishers,
            'num_books': num_books,
            'num_stores': num_stores,
        }
    )


def author(request):
    author_list = Author.objects.annotate(num_books=Count('book'))
    return render(
        request,
        'bookstore/author.html',
        context={
            'author_list': author_list,
        }
    )


def author_detail(request, pk):
    author_instance = Author.objects.prefetch_related('book_set').get(pk=pk)
    author_books = list(author_instance.book_set.all())
    return render(
        request,
        'bookstore/author_detail.html',
        context={
            'author_instance': author_instance,
            'author_books': author_books,
        }
    )


def publisher(request):
    publisher_list = Publisher.objects.annotate(num_books=Count('book'))
    return render(
        request,
        'bookstore/publisher.html',
        context={
            'publisher_list': publisher_list,
        }
    )


def publisher_detail(request, pk):
    publisher_instance = Publisher.objects.annotate(avg_rating=Avg('book__rating')).get(pk=pk)
    publisher_books = list(publisher_instance.book_set.all())
    return render(
        request,
        'bookstore/publisher_detail.html',
        context={
            'publisher_instance': publisher_instance,
            'publisher_books': publisher_books,
        }
    )


def book(request):
    book_list = Book.objects.select_related("publisher").prefetch_related('authors').all()
    return render(
        request,
        'bookstore/book.html',
        context={
            'book_list': book_list,
        }
    )


def book_detail(request, pk):
    book_instance = Book.objects.select_related("publisher").prefetch_related('authors').get(pk=pk)
    book_authors = list(book_instance.authors.all())
    return render(
        request,
        'bookstore/book_detail.html',
        context={
            'book_instance': book_instance,
            'book_authors': book_authors,
        }
    )


def store(request):
    store_list = Store.objects.annotate(num_books=Count('books'))
    return render(
        request,
        'bookstore/store.html',
        context={
            'store_list': store_list,
        }
    )


def store_detail(request, pk):
    store_instance = Store.objects.annotate(avg_rating=Avg('books__rating'), avg_price=Avg('books__price')).get(pk=pk)
    store_books = list(store_instance.books.all())
    return render(
        request,
        'bookstore/store_detail.html',
        context={
            'store_instance': store_instance,
            'store_books': store_books,
        }
    )
