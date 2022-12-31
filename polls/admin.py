from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = 'Farshid Admin'


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QustionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['question_text', 'pub_date']})
    ]

    inlines = ChoiceInline,

    list_display = ('question_text', 'pub_date', 'published_recently')

    list_filter = ('pub_date',)
    search_fields = ('question_text',)


admin.site.register(Question, QustionAdmin)
admin.site.register(Choice)
