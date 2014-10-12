import random 
import math

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
from django.db.models import Max, F

from extra_views import ModelFormSetView

from forms import AttemptForm

def success_proportion_on_level(curr_learner):
    '''
    Determines what proportion of `Word` at the current
    `learner_level` for this `Learner` were answered
    successfully at the the most recent `Attempt` by this
    `Learner`.
    '''

    #How many words are in this level
    cnt_words_in_lvl = Word.objects.filter(
                        source=curr_learner.source
                    ).filter(
                        level=curr_learner.learning_level
                    ).count()

    #How many words in this level were successfully spelt
    #the last time an attempt was made to do so
    cnt_words_in_lvl_last_got_right = Word.objects.filter(
                        source=curr_learner.source
                    ).filter(
                        level=curr_learner.learning_level
                    ).annotate(
                        latest=Max('attempt__when')
                    ).filter(
                        attempt__success=True, attempt__when=F('latest')
                    ).count()

    proportion_last_right_in_lvl = float(cnt_words_in_lvl_last_got_right) / float(cnt_words_in_lvl) 

    return proportion_last_right_in_lvl

def increase_learner_level(curr_learner):
    '''
    Returns a boolean indicating whether, based on results
    so far, the `learning_level` for a `Learner`, passed
    as argument `curr_learner`, should be raised
    '''
    LEVELUPTHOLD = 0.5 
    succ_prop_on_lvl = success_proportion_on_level(curr_learner)

    if succ_prop_on_lvl > LEVELUPTHOLD:
        return True
    else:
        return False


def generate_weightings(lvl, fresh_words, stale_words, recent_successes, recent_failures): 
    '''
    Populates a dictionary with one element for each word which is a candidate
    for inclusion on the attempts page. The value of each element is a number
    which will specify how likely that word is to appear on the next page

    It's assumed that the Querysets fresh_words and stale_words together contain
    all the words which the current user might be asked to spell

    '''

    #The spacing of the weighting constants is partially determined by
    #how many levels might appear within a certain source. I'm going to 
    #assume there will be no more than 15 levels
    FRESHWORD = 30
    STALEWORD = 15
    HIDERECENTSUCCESS = 0.25
    PROMOTERECENTFAILURE = 4.00

    weighting = {}
    for word in fresh_words:
        weighting[word.id] = FRESHWORD * ((word.level * -1) + lvl + 1 ) 
    for word in stale_words:
        weighting[word.id] = STALEWORD * ((word.level * -1) + lvl + 1 ) 
    for word in recent_successes:
        weighting[word.id] = weighting[word.id] * HIDERECENTSUCCESS 
    for word in recent_failures:
        weighting[word.id] = weighting[word.id] * PROMOTERECENTFAILURE 

    for k, v in weighting.iteritems():
        weighting[k] = int(math.floor(weighting[k]))

    print weighting
    return weighting

def make_weighted_attempt_set(src, curr_learner, max_cnt=10, repeat_depth=4):
    '''
    Return a list of dictionaries. 
    
    The content of each dictionary relates to a single word.

    Each word is chosen from the subset of all words within 
    the `src` set which are at or below the `Learner` level value.

    Words are chosen from that set and may be viewed as two subsets.

    The first subset contains words which have been attempted
    recently but which the user seems to have trouple spelling.

    The second subset contains words which have been attempted
    recently and which the user seems to be able to spell.

    The relative sizes of these two sets is dependent on the
    results of the most recent set of attempts. Where a user
    had difficultly with the last set the next set will tend
    to skew towards those words they have previously succeeded
    with. By contrast where the user is doing well a greater
    number of more complex words will be included in the next 
    set

     * Simplicity (Simplest have lowest level)
     * Results by this user of most recent attempt on the `Word`
     * Whether there has been a failure in the most
       recent `repeat_depth` attempts by this user

    '''

    count = Word.objects.filter(
                        source=curr_learner.source
                    ).filter(
                        level=curr_learner.learning_level
                    ).count()

    if max_cnt < count:
        count = max_cnt
    else:
        if count > 5:
            count = int(math.floor(count * 0.5))


    recent_attempts = Attempt.objects.filter(
                        learner=curr_learner.id
                    ).filter(
                        word__source=src
                    ).order_by('-when')[:count]

    success_ids = []
    fail_ids = []

    for attempt in recent_attempts:
        if attempt.success:
            success_ids.append(attempt.id)
        else:
            fail_ids.append(attempt.id)

    #Words they succeeded with last time
    recent_successes = Word.objects.filter(attempt__in=success_ids).distinct()

    #Words they failed with last time
    recent_failures = Word.objects.filter(attempt__in=fail_ids).distinct()

    #Words they have yet to attempt within the users level
    fresh_words = Word.objects.filter(
                        attempt__isnull=True
                    ).filter(
                        source=src
                    ).filter(
                        level__lte=curr_learner.learning_level
                    ).filter(
                        level__gte=curr_learner.starting_level
                    ).distinct()

    #Words they have attempted at some point
    stale_words = Word.objects.filter(
                        attempt__isnull=False
                    ).filter(
                        source=src
                    ).filter(
                        level__lte=curr_learner.learning_level
                    ).filter(
                        level__gte=curr_learner.starting_level
                    ).distinct()

    weighting = generate_weightings(curr_learner.learning_level, fresh_words, stale_words, recent_successes, recent_failures) 

    pk_list = []
    values_found = 0
    while values_found < count:
        choice_id = random.choice([k for k in weighting for dummy in range(weighting[k])])
        if choice_id in pk_list:
            pass
        else:
            pk_list.append(choice_id)
            values_found += 1

    init_data = []
    words_set_qs = Word.objects.all().filter(
                    id__in=pk_list
                )

    for word in words_set_qs:
        init_data.append({'word': word.word, 'hint': word.hint, 'wordid': word.pk})



    print("Success in last attempt: {cntsuccess:d}".format(cntsuccess=len(recent_successes)))
    print("Failure in last attempt: {cntfailure:d}".format(cntfailure=len(recent_failures)))
    print("Fresh words: {freshwords:d}".format(freshwords=len(fresh_words)))
    print("Stale words: {stalewords:d}".format(stalewords=len(stale_words)))
    print pk_list

    return init_data

def make_random_attempt_set(lvl, src, count=10):
    '''
    Return a list of dictionaries. The content
    of each dictionary relates to  a single word randomly
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
    curr_learner = Learner.objects.get(id=request.user.id)

    context = RequestContext(request)

    AttemptFormSet = formset_factory(AttemptForm, extra=0)
    formset = AttemptFormSet(initial=make_weighted_attempt_set(curr_learner.source, curr_learner, max_cnt=10))

    return render_to_response('spellweb/attempt_add.html', {'formset': formset}, context)


def attempt_submission(request):
    '''
    Parse the form contents; Add corresponding `Attempt` objects;
    If necessary adjust `learning_level` property on the users
    `Learner` object
    '''

    AttemptFormSet = formset_factory(AttemptForm, extra=0)
    formset = AttemptFormSet(request.POST)

    lstAttempts = []
    if(formset.is_valid()):
        curr_learner = Learner.objects.get(id=request.user.id)
        #Add Attempt objects
        for form in formset:
            d = form.cleaned_data
            word_qs = Word.objects.get(id=d['wordid'])
            lstAttempts.append(Attempt(learner=curr_learner, word=word_qs, success=d['success']))
        Attempt.objects.bulk_create(lstAttempts)
        #Potentially adjust `learning_level` value for this `Learner`
        if increase_learner_level(curr_learner):
            print "About to up learner_level"
            curr_learner.learning_level=curr_learner.learning_level + 1
            curr_learner.save()
    
        dic_context={}
        dic_context['test_uname'] = request.user.get_username()
        context = dic_context
        return render(request, 'spellweb/attempt_submission_confirm.html', context)
    else:
        return HttpResponse("An unexpected error occurred. Please report this situation.")

class IndexView(generic.ListView):
    def get(self, request, *args, **kwargs):
        dic_context={}
        dic_context['test_uname'] = request.user.get_username()

        curr_learner = Learner.objects.get(id=request.user.id)
        context = dic_context
        context['lrng_lvl'] = curr_learner.learning_level
        context['word_set'] = curr_learner.source
        '''
        If the user hasn't yet set up a Learner then direct them to do so 
        now 
        '''
        try:
            l = Learner.objects.get(username = request.user.get_username())
        except Learner.DoesNotExist:
            return redirect('lc/', request )

        return render(request, 'spellweb/index.html', context)

class LearnerCreate(CreateView):
    model = Learner
    success_url='/spellweb/'

    def get_initial(self):
        dic = {'username': self.request.user.get_username()} 
        self.initial = dic
        return self.initial
        

