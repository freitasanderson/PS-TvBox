from django.views.generic import DetailView
from desafios.models.Trilha import Trilha

class TrilhaDetailView(DetailView):
    model = Trilha
    template_name = 'trilhaDetailView.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    