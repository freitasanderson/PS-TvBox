from django.views.generic.list import ListView
from desafios.models import Desafio, Trilha, Submissao
from desafios.forms import SubmissaoForm
from django.contrib.auth.mixins import LoginRequiredMixin

class DesafiosListView(LoginRequiredMixin, ListView):
    model = Trilha
    template_name = 'desafiosListView.html'

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      submissoes = Submissao.objects.filter(problema__in=Desafio.objects.all(), pessoa__user=self.request.user)
      context['data'] = self.getDataSubmissoes(submissoes)
      context['submissoes'] = submissoes
      context['submissoesCorretas'] = submissoes.filter(resultado=1).count()
      if submissoes:
        context['porcentagem'] = (100 * len(submissoes.filter(resultado=1)) / submissoes.count())
      return context

    def getDataSubmissoes(self, submissoes):
      data = []
      meses = [4, 5, 6, 7, 8, 9]
      
      for mes in meses:
        _data = 0
      
        for submissao in submissoes:
            # print(submissao.dataSubmissao.month, mes)
            if submissao.dataSubmissao.month == mes:
                _data += 1
        data.append(_data)
    

        