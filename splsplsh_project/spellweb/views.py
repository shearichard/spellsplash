from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect

from spellweb.models import Learner
from .forms import AttemptFormSet, LearnerTestForm

from django.views.generic.edit import CreateView

class RecipeCreateView(CreateView):
    template_name = 'spellweb/attempt_add.html'
    model = Learner
    form_class = LearnerTestForm
    success_url = 'success/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        attempt_form = AttemptFormSet()
        return self.render_to_response(self.get_context_data(form=form, attempt_form=attempt_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        attempt_form = AttemptFormSet(self.request.POST)
        if (form.is_valid() and attempt_form.is_valid()):
            return self.form_valid(form, attempt_form)
        else:
            return self.form_invalid(form, attempt_form)

    def form_valid(self, form, attempt_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        attempt_form.instance = self.object
        attempt_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, attempt_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(self.get_context_data(form=form, attempt_form=attempt_form))

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
        

