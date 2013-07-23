from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class PollAdmin(admin.ModelAdmin):
  # fields = ['pub_date', 'question']
  list_display = ('question', 'pub_date', 'was_published_recently')
  fieldsets = [(None, {'fields': ['question']}),
            ('Date information', {'fields': ['pub_date'],
                                  'classes': ['collapse']})
            ]
  inlines = [ChoiceInline]

# By registering the Poll model with admin.site.register(Poll),
# Django is able to construct a default form representation.
admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)
