from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('search', views.SearchListView.as_view(), name='search'),
    path('book/<pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('book/<int:book_id>/delete', views.delete_book, name='book-delete'),
]