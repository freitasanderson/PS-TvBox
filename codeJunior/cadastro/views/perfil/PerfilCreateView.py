from django.views.generic.edit import CreateView

from codeJunior.cadastro.models import Perfil

class PerfilCreateView(CreateView):
    model = Perfil
    fields = ['nome', 'pessoa', 'imagem', 'ativo']
    template_name = ''

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        pass
