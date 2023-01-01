from django.contrib import admin
from .models import *


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = ChoiceInline,

