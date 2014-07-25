from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
from django.forms.formsets import formset_factory
from django.template import RequestContext

from spellweb.models import Learner, Attempt

from django.views.generic.edit import CreateView

from extra_views import ModelFormSetView

from forms import AttemptForm

def make_init():
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

    '''
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()
    '''
    AttemptFormSet = formset_factory(AttemptForm)
    formset = AttemptFormSet(initial=make_init())
    '''


    for form in formset:
        print(form.as_p())
    
    
    return HttpResponse("You're looking at attempt_create")

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    '''

    return render_to_response('spellweb/attempt_add_a.html', {'form': formset}, context)

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
        

