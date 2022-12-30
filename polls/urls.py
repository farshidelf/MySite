from django.urls import path
from django.views.generic import TemplateView

app_name = 'polls'
urlpatterns = [
    path('', TemplateView.as_view(template_name='polls/index.html'), name='index'),
]