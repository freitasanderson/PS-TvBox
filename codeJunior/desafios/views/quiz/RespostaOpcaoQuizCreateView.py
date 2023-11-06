from django.views.generic import CreateView
from django.shortcuts import redirect
#
from desafios.models import RespostaQuiz
from desafios.forms import RespostaOpcaoQuizCreateForm

class RespostaOpcaoQuizCreateView(CreateView):
  model = RespostaQuiz
  form_class = RespostaOpcaoQuizCreateForm
  
  def form_valid(self, form):
      resposta = form.save(commit=False)
      resposta.quemRespondeu = self.request.user.pessoa
      resposta.save()
      return super().form_valid(form)

  def form_invalid(self, form):
    print(form.errors)
    return redirect(self.request.META['HTTP_REFERER'])

  def get_success_url(self):
     return self.request.META['HTTP_REFERER']
  

    

        