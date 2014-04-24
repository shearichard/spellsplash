from django.contrib import admin
from spellweb.models import Teacher 
from spellweb.models import Learner 
from spellweb.models import Word    
from spellweb.models import Attempt 

admin.site.register(Teacher)
admin.site.register(Learner)
admin.site.register(Word)
admin.site.register(Attempt)

# Register your models here.
