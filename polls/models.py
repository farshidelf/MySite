from django.db import models
from django.contrib import admin


class Author(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ManyToManyField(Author)
    summary = models.TextField()


    @admin.display(
        description='Authors'
    )
    def author_list(self):
        return ', '.join([author.name for author in self.author.all()])

    def __str__(self):
        return self.title