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
        try:
            l = Learner.objects.get(username = request.user.get_username())
            print "Yes"
        except Learner.DoesNotExist:
            print "No"
            #return redirect('MyViewLearner', request)
            #return redirect('anamedurl', request)
            return redirect('lc/', request )
        return render(request, 'splsplsh_project/index.html', context)
        #return HttpResponse("Hello, World")

#class DetailView(generic.DetailView):
#    pass
#
#class ResultsView(generic.DetailView):
#    pass
#
class LearnerCreate(CreateView):
    model = Learner
    fields = ['teacher', 'learning_level']
    success_url='/spellweb/'

class MyViewLearner(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, Learner 9")

