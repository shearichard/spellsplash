from django.contrib import admin
from spellweb.models import Teacher 
from spellweb.models import Learner 
from spellweb.models import Word    
from spellweb.models import Attempt 
from spellweb.models import Box     

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('chosen_name', 'family_name')

class LearnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'learning_level', 'family_name', 'chosen_name')

class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'level', 'source')
    list_filter = ('source',)

class AttemptAdmin(admin.ModelAdmin):
    list_filter = ['learner']
    list_display = ('word', 'learner', 'when', 'success')

class BoxAdmin(admin.ModelAdmin):
    list_display = ('box_number', 'learner', 'word')
    list_filter = ('learner',)

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Learner, LearnerAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Attempt, AttemptAdmin)
admin.site.register(Box, BoxAdmin)

