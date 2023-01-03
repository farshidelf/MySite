from django import forms
from .models import *

from .my_vals import validate_question



class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = ('text',)

    
    def clean_text(self):
        data = self.cleaned_data['text']
        # validate_question(data)

        if not (data.lower().startswith('w') and data.lower().endswith('?')):
            raise forms.ValidationError('v')
        return data


class VForm(forms.Form):
    name = forms.CharField(max_length=6)

    def clean_name(self):
        data = self.cleaned_data['name']
        validate_question(data)

        # if not (data.lower().startswith('w') and data.lower().endswith('?')):
        #     raise forms.ValidationError('v')
        return data
    
        