from django.urls import path
from desafios.views import SubmissaoCreateView, DesafiosResolvidosListView, DesafiosListView, DesafiosDetailView

from desafios.views import QuizTentativaDetailView, RespostaOpcaoQuizCreateView

from desafios.views import BibliotecaListView

from cadastro.views import LoginView, SairView, CadastroView

urlpatterns = [
    path('', DesafiosListView.as_view(), name="desafios-list"),
    path('desafio/<int:pk>', DesafiosDetailView.as_view(), name="desafios-detail"),
    path('tentativa/', SubmissaoCreateView.as_view(), name='submeterTentativa'),
    path('resultado/', DesafiosResolvidosListView.as_view(), name='desafioResolvido'),

    path('quiz/<slug:slug>/', QuizTentativaDetailView.as_view(), name="quiz-tentativa"),
    path('quiz/<int:pk>/resposta/', RespostaOpcaoQuizCreateView.as_view(), name="quiz-resposta-create"),

    path('biblioteca/', BibliotecaListView.as_view(), name='biliotecaList'),
    
    #Logins views
    path('login/', LoginView.as_view(), name='login'),
    path('sair/', SairView.as_view(), name='sair'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
]
