from django.contrib import admin

from .models import Question, Choice


admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to pollster area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3   # Extra fields


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}), 
    ('Date information', {'fields': ['published_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)
