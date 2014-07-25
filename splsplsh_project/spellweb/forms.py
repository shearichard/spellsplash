# forms.py
from django.forms import ModelForm, Form, CharField, BooleanField
from django.forms.models import inlineformset_factory

from .models import Learner, Word, Attempt 

class AttemptForm(Form):
    word = CharField()
    success = BooleanField()
