from django import forms
from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', 'owner')

    
        