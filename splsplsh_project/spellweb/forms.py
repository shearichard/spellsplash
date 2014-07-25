# forms.py
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Learner, Word, Attempt 


class LearnerTestForm(ModelForm):
    class Meta:
        model = Learner

AttemptFormSet = inlineformset_factory(Learner, Attempt)
