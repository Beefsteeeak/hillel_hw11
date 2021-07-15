import random

from django.core.management.base import BaseCommand

from faker import Faker

from rediscache.models import Author, Book

fake = Faker()


class Command(BaseCommand):
    """
    This command is for inserting Author, Book into database.
    """

    def handle(self, *args, **options):
        Author.objects.all().delete()
        Book.objects.all().delete()

        # create 500 authors
        authors = [Author(name=fake.unique.name(), age=random.randint(20, 80)) for _ in range(500)]
        Author.objects.bulk_create(authors)

        # create 2000 books
        books = [Book(name=fake.unique.catch_phrase(), pages=random.randint(150, 800), price=random.randint(50, 300),
                      rating=round(random.uniform(0, 10), 2), pubdate=fake.date()) for _ in range(2000)]
        Book.objects.bulk_create(books)

        #  create MTM relations from Book to Author
        authors = list(Author.objects.all())
        for books in Book.objects.all():
            temp_authors = random.sample(authors, 4)
            books.authors.set(temp_authors)
