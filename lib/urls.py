from django.urls import path
from . import views

app_name = 'lib'
urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('author/', views.AuthorListView.as_view(), name='author-list'),
    path('add_book/', views.CreateBookView.as_view(), name='book-add'),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('book/<pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('book/<pk>/update/', views.UpdateBookView.as_view(), name='book-update'),
    path('book/<int:book_id>/delete/', views.delete_book, name='book-delete'),
    path('author/<int:author_id>/delete/', views.delete_author, name='author-delete'),
]