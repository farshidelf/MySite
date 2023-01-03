from django.db import models
from django.contrib.auth.models import User

from .my_vals import validate_question


class Question(models.Model):
    text = models.CharField(max_length=400)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)


    class Meta:
        permissions = (
            ('can_add', 'Can Add Question'),
        )

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=400)
    votes = models.PositiveSmallIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
