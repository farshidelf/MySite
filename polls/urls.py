from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.QuestionListView.as_view(), name='index'),
    path('my_questions/', views.MyQuestionListView.as_view(), name='my-questions'),
    path('vform/',views.vform),
    # path('add_question/', views.add_question, name='question-add'),
    path('add_question/', views.QuestionCreateView.as_view(), name='question-add'),
    path('<pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('<int:question_id>/edit_choices/', views.AddChoiceToQuestion.as_view(), name='choices-edit'),
    path('<int:question_id>/<int:choice_id>/delete/', views.delete_choice, name='choice-delete'),
    path('<int:question_id>/update/', views.update_question, name='question-update'),
    # path('<pk>/update/', views.QuestionUpdateView.as_view(), name='question-update'),
    path('<int:question_id>/delete', views.delete_question, name='question-delete'),
    path('<int:question_id>/vote', views.vote_question, name='question-vote'),
    
]