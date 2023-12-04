from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from forum.models import Post, Secao, SubSecao,Topico
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class TopicoCreateView(LoginRequiredMixin,TemplateView):
    template_name="TopicoCreate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        secao = kwargs.get('pkSecao')

        secaoObj = Secao.objects.get(id=secao)

        subsecao = kwargs.get('pkSubsecao')

        subSecaoObj = SubSecao.objects.get(id=subsecao) if subsecao else None

        context["post"] = SummernoteTextField()

        context["secao"] = secaoObj
        context["subSecao"] = subSecaoObj 

        # print(f'Secao: {secao} e Subsecao: {subsecao}')
        
        return context