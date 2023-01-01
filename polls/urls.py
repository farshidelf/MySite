from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.QuestionListView.as_view(), name='index'),
    path('add_question/', views.add_question, name='question-add'),
    path('<pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('<int:question_id>/delete', views.delete_question, name='question-delete'),
    path('<int:question_id>/vote', views.vote_question, name='question-vote'),
]