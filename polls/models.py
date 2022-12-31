from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('Publish Date')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='-pub_date',
        description='Is Poblished in 2 days?'
    )
    def published_recently(self):
        return timezone.now() - timedelta(days=2) < self.pub_date < timezone.now()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)

    def __str__(self):
        return self.choice_text