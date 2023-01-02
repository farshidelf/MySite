from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from .forms import *


class QuestionListView(ListView):
    model = Question
    paginate_by = 3
    ordering = '-created'


class QuestionDetailView(DetailView):
    model = Question


def delete_question(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    q.delete()

    return redirect(reverse('polls:index'))


def vote_question(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choices.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            messages.error(request, 'Please Select One choice!!')
            return redirect(reverse('polls:question-detail', args=(question_id,)))

        selected_choice.votes += 1
        selected_choice.save()

        return redirect(reverse('polls:question-detail', args=(question_id,)))
    return redirect(reverse('polls:question-detail', args=(question_id,)))

def index(request):
    return redirect(reverse('index'))


def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.owner = request.user
            question.save()
            messages.success(request, 'Question Added Successfully!!')
            return redirect(reverse('polls:index'))

    form = QuestionForm()

    context = {
        'form': form
    }
    return render(request, 'polls/add_question.html', context=context)


class QuestionUpdateView(UpdateView):
    model = Question

    fields = 'text',
    success_url = '/polls/'
