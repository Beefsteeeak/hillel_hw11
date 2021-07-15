import random

from bookstore.models import Author, Book, Publisher, Store

from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    """
    This command is for inserting Author, Book, Publisher, Store into database.
    """

    def handle(self, *args, **options):
        Author.objects.all().delete()
        Book.objects.all().delete()
        Publisher.objects.all().delete()
        Store.objects.all().delete()

        # create 20 authors
        authors = [Author(name=f"Author{index}", age=random.randint(20, 80)) for index in range(1, 21)]
        Author.objects.bulk_create(authors)

        # create 5 publishers
        publishers = [Publisher(name=f"Publisher{index}") for index in range(1, 6)]
        Publisher.objects.bulk_create(publishers)

        # create 20 books for every publishers
        counter = 0
        books = []
        for publisher in Publisher.objects.all():
            for i in range(20):
                counter = counter + 1
                books.append(Book(name=f"Book{counter}", pages=random.randint(150, 800), price=random.randint(50, 300),
                                  rating=round(random.uniform(0, 10), 2), publisher=publisher, pubdate=fake.date()))
        Book.objects.bulk_create(books)

        #  create MTM relations from Book to Author
        authors = list(Author.objects.all())
        for books in Book.objects.all():
            temp_authors = random.sample(authors, 5)
            books.authors.set(temp_authors)

        # create 10 stores and insert 10 books in every store
        books = list(Book.objects.all())
        for i in range(10):
            temp_books = random.sample(books, 10)
            store = Store.objects.create(name=f"Store{i + 1}")
            store.books.set(temp_books)
