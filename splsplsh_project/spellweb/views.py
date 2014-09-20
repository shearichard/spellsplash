import random 

from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
from django.forms.formsets import formset_factory
from django.template import RequestContext

from spellweb.models import Word, Learner, Attempt

from django.views.generic.edit import CreateView

from extra_views import ModelFormSetView

from forms import AttemptForm

def make_random_attempt_set(lvl, src, count=10):
    '''
    Return a list of dictionaries. The content
    of each dictionary is a single word randomly
    selected from the set of Word objects filtered
    by the level passed as an argument
    '''
    init_data = []
    slicetop = count - 1
    words_set_qs = Word.objects.all().filter(
                    level=lvl
                ).filter(
                    source=src
                )

    if len(words_set_qs) < count:
        for word in words_set_qs:
            init_data.append({'word': word.word, 'hint': word.hint, 'wordid': word.pk})
    else:
        pk_list = []
        values_found = 0
        while values_found < count:
            choice_id = random.randrange(0, (len(words_set_qs) - 1) )
            if choice_id in pk_list:
                pass
            else:
                pk_list.append(choice_id)
                word = words_set_qs[choice_id]
                init_data.append({'word': word.word, 'hint': word.hint, 'wordid': word.pk})
                values_found += 1
    return init_data


def make_hardcoded_attempt_set():
    '''
    Return a list of dictionaries. The content
    of each dictionary is a single hardcoded word
    '''
    init_data = []
    init_data.append({'word':'azzzzzzzzzzzz'})
    init_data.append({'word':'bzzzzzzzzzzzz'})
    init_data.append({'word':'czzzzzzzzzzzz'})
    init_data.append({'word':'dzzzzzzzzzzzz'})
    init_data.append({'word':'ezzzzzzzzzzzz'})
    init_data.append({'word':'fzzzzzzzzzzzz'})
    init_data.append({'word':'gzzzzzzzzzzzz'})
    init_data.append({'word':'hzzzzzzzzzzzz'})
    init_data.append({'word':'izzzzzzzzzzzz'})
    init_data.append({'word':'jzzzzzzzzzzzz'})
    init_data.append({'word':'kzzzzzzzzzzzz'})
    return init_data

def attempt_create(request):
    context = RequestContext(request)

    AttemptFormSet = formset_factory(AttemptForm, extra=0)
    formset = AttemptFormSet(initial=make_random_attempt_set(lvl=0, src="OT", count=10))

    return render_to_response('spellweb/attempt_add.html', {'formset': formset}, context)


def attempt_submission(request):
    current_user = request.user
    curr_learner_qs = Learner.objects.get(id=current_user.id)

    AttemptFormSet = formset_factory(AttemptForm, extra=0)
    formset = AttemptFormSet(request.POST)

    lstAttempts = []
    if(formset.is_valid()):
        for form in formset:
            d = form.cleaned_data
            word_qs = Word.objects.get(id=d['wordid'])
            lstAttempts.append(Attempt(learner=curr_learner_qs, word=word_qs, success=d['success']))
        Attempt.objects.bulk_create(lstAttempts)
    
    return HttpResponse("You've submitted your attempt")

class IndexView(generic.ListView):
    def get(self, request, *args, **kwargs):
        dic_context={}
        dic_context['test_uname'] = request.user.get_username()
        context = dic_context
        '''
        If the user hasn't yet set up a Learner then direct them to do so 
        now 
        '''
        try:
            l = Learner.objects.get(username = request.user.get_username())
        except Learner.DoesNotExist:
            return redirect('lc/', request )

        return render(request, 'spellweb/index.html', context)

#class DetailView(generic.DetailView):
#    pass
#
#class ResultsView(generic.DetailView):
#    pass
#

class LearnerCreate(CreateView):
    model = Learner
    success_url='/spellweb/'

    def get_initial(self):
        dic = {'username': self.request.user.get_username()} 
        self.initial = dic
        return self.initial
        

