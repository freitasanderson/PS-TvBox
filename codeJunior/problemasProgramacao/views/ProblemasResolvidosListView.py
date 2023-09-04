import subprocess
from django.views.generic.list import ListView
from problemasProgramacao.models.Problema import Problema
from problemasProgramacao.forms import SubmissaoForm

class ProblemasResolvidosListView(ListView):
    model = Problema
    template_name = 'problemasResolvidos.html'

        