from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class QuestionListView(ListView):
    model = Question
    paginate_by = 3
    ordering = '-modify'


class MyQuestionListView(LoginRequiredMixin, ListView):
    model = Question
    paginate_by = 3
    ordering = '-modify'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)

@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.owner:
        question.delete()
        messages.success(request, f'{question} deleted!')
    else:
        messages.warning(request, 'You dont own this question')
    return redirect(reverse('polls:my-questions'))


def vote_question(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choices.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            messages.warning(request, 'Please Select One choice!!')
            return redirect(reverse('polls:question-detail', args=(question_id,)))

        selected_choice.votes += 1
        selected_choice.save()

        return redirect(reverse('polls:question-detail', args=(question_id,)))
    return redirect(reverse('polls:question-detail', args=(question_id,)))


def index(request):
    return redirect(reverse('index'))


# @permission_required('can_add')
# def add_question(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             if request.user.is_authenticated:
#                 question.owner = request.user
#             question.save()
#             messages.success(request, 'Question Added Successfully!!')
#             return redirect(reverse('polls:index'))

#     form = QuestionForm()

#     context = {
#         'form': form
#     }
#     return render(request, 'polls/add_question.html', context=context)


class QuestionCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Question
    form_class = QuestionForm
    success_url = reverse_lazy('polls:index')
    permission_required = 'polls.can_add'
    raise_exception = False
    success_message = "%(question_text)s was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            question_text=self.object.text,
        )

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(QuestionCreateView, self).form_valid(form)


class QuestionUpdateView(UpdateView):
    model = Question

    fields = 'text',
    success_url = reverse_lazy('polls:index')


def update_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.owner:
        form = QuestionForm(request.POST or None, instance=question)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
        return render(request, 'polls/question_form.html', {'form': form})
    messages.warning(request, 'You dont own this question')
    return redirect(reverse('polls:index'))


def vform(request):
    form = VForm()
    if request.method == 'POST':
        form = VForm(request.POST)
    return render(request, 'polls/vform.html', {'form': form})


class AddChoiceToQuestion(CreateView):
    model = Choice
    form_class = ChoiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = Question.objects.get(pk=self.kwargs['question_id'])
        context['question'] = question
        context['all_choices'] = question.choices.all().order_by('-votes')
        return context

    def form_valid(self, form):
        form.instance.question = Question.objects.get(
            pk=self.kwargs['question_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('polls:question-detail', args=(self.kwargs['question_id'],))


def delete_choice(request, question_id, choice_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = question.choices.get(pk=choice_id)
    choice.delete()
    return redirect(reverse('polls:choices-edit', args=(question_id,)))
