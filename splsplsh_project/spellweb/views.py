from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from spellweb.models import Word, Attempt


class IndexView(generic.ListView):
    def get(self, request, *args, **kwargs):
        context = {'test_message': "This is content, Hello, World"}
        return render(request, 'splsplsh_project/index.html', context)
        #return HttpResponse("Hello, World")

#class DetailView(generic.DetailView):
#    pass
#
#class ResultsView(generic.DetailView):
#    pass
#

