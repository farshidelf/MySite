from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'summary', 'author_list']

admin.site.register(Author)
admin.site.register(Book, BookAdmin)