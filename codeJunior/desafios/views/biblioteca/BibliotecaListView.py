from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from desafios.models import TipoTutorial, Tutorial

class BibliotecaListView(LoginRequiredMixin, TemplateView):
    template_name = 'bibliotecaListView.html'

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      tipos = TipoTutorial.objects.filter(ativo=True)

      context['tipos'] = tipos

      return context

        