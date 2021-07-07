from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
