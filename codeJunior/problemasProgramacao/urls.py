from django.urls import path
from .views import SubmissaoCreateView, ProblemasResolvidosListView

urlpatterns = [
    path('submeter-tentativa/', SubmissaoCreateView.as_view(), name='submeterTentativa'),
    path('problemas-resolvidos/', ProblemasResolvidosListView.as_view(), name='problemasResolvidos'),
]
