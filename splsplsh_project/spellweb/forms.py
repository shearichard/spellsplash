# forms.py
from django.forms import ModelForm, Form, CharField, BooleanField, TextInput
from django.forms.models import inlineformset_factory

from .models import Learner, Word, Attempt 

class AttemptForm(Form):
    word = CharField(widget=TextInput(attrs={'readonly':'readonly'}))
    success = BooleanField()
