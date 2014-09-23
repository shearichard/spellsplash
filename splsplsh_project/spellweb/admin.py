from django.contrib import admin
from spellweb.models import Teacher 
from spellweb.models import Learner 
from spellweb.models import Word    
from spellweb.models import Attempt 

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('chosen_name', 'family_name')

class LearnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'learning_level', 'family_name', 'chosen_name')

class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'level', 'source')
    list_filter = ('source',)

class AttemptAdmin(admin.ModelAdmin):
    list_display = ('word', 'when', 'success')

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Learner, LearnerAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Attempt, AttemptAdmin)

