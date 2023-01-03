from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.UserCreateView.as_view(), name='register'),
]