from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import permission_required


class QuestionListView(ListView):
    model = Question
    paginate_by = 5
    ordering = '-modify'


class QuestionDetailView(DetailView):
    model = Question


def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.owner:
        question.delete()
        messages.success(request,f'{question} deleted!')
    else:
        messages.error(request,'You dont own this question')
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

@permission_required('can_add')
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            if request.user.is_authenticated:
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


def update_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.owner:
        form = QuestionForm(request.POST or None, instance=question)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
        return render(request, 'polls/question_form.html', {'form': form})
    messages.error(request,'You dont own this question')
    return redirect(reverse('polls:index'))

def vform(request):
    form = VForm()
    if request.method == 'POST':
        form = VForm(request.POST)
    return render(request, 'polls/vform.html',{'form':form})
