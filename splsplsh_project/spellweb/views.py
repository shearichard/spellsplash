from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect

from spellweb.models import Word, Attempt, Learner

from django.views.generic.edit import CreateView

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
        return render(request, 'splsplsh_project/index.html', context)

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
        

