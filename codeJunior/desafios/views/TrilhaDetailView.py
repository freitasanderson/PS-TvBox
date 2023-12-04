from django.views.generic import DetailView
from desafios.models import Trilha, Submissao

class TrilhaDetailView(DetailView):
    model = Trilha
    template_name = 'trilhaDetailView.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        trilha = self.get_object()
        desafios = trilha.desafios.all()

        totalSubmissoes = Submissao.objects.filter(problema__in=desafios).count()

        respostasCorretas = Submissao.objects.filter(problema__in=desafios, resultado=1).count()
        
        porcentagemCorretas = 0

        if totalSubmissoes > 0:
            porcentagemCorretas = round((respostasCorretas / totalSubmissoes) * 100, 2)
        else:
            porcentagemCorretas = 0

        context['trilhasDisponiveis'] = Trilha.objects.all()
        context['totalSubmissoes'] = totalSubmissoes
        context['porcentagemCorretas'] = porcentagemCorretas

        return context
