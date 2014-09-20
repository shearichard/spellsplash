# forms.py
from django.forms import ModelForm, Form, CharField, BooleanField, TextInput
from django.forms.models import inlineformset_factory, ModelForm

from .models import Learner, Word, Attempt 

class AttemptForm(Form):

    word = CharField(required=False)
    success = BooleanField(required=False)
    wordid = CharField()
