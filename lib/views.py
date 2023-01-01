from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from django.db.models import Q
from django.urls import reverse

from .models import *


class SearchListView(View):
    def get(self, request):
        return redirect(reverse('lib:index'))

    def post(self, request):
        if q:= Book.objects.filter(Q(title__contains=request.POST['searched']) | Q(author__name__icontains=request.POST['searched'])).all():
            book_list = set(q)
        else:
            book_list = None
        context = {
            'book_list': book_list
        }
        return render(request, 'lib/book_list.html', context=context)


# class SearchListView(ListView):
#     model = Book

#     def get_queryset(self):
#         return Book.objects.filter(Q(title__contains=self.request.GET['searched']) | Q(author__name__icontains=self.request.GET['searched'])).all()

def delete_book(request, book_id):
    Book.objects.get(pk=book_id).delete()

    return redirect(reverse('lib:index'))


def delete_author(request, author_id):
    Author.objects.get(pk=author_id).delete()

    return redirect(reverse('lib:author-list'))

    
class BookListView(ListView):
    model = Book
    paginate_by = 3


class AuthorListView(ListView):
    model = Author


class BookDetailView(DetailView):
    model = Book


class AuthorDetailView(DetailView):
    model = Author


class CreateBookView(CreateView):
    model = Book

    fields = 'title', 'author', 'summary'
    success_url = '/lib/'


class UpdateBookView(UpdateView):
    model = Book

    fields = 'title', 'author', 'summary'
    success_url = '/lib/'


def index(request):
    pass
