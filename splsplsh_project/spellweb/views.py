from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
from django.forms.formsets import formset_factory

from spellweb.models import Learner, Attempt

from django.views.generic.edit import CreateView

from extra_views import ModelFormSetView

from forms import AttemptForm

def attempt_create(request):
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

    AttemptFormSet = formset_factory(AttemptForm)
    formset = AttemptFormSet(initial=init_data)

    for form in formset:
        print(form.as_table())
    return HttpResponse("You're looking at attempt_create")

class IndexView(generic.ListView):
    def get(self, request, *args, **kwargs):
        dic_context = {'test_message': "This is content, Hello, World"}
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

        return render(request, 'spellweb/base.html', context)

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
        

