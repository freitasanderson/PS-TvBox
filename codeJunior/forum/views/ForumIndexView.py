from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from forum.models import Area, Post, Secao, SubSecao,Topico

class ForumIndexView(LoginRequiredMixin,TemplateView):
    template_name="ForumIndex.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        areas = Area.objects.all()

        for area in areas:
            
            secoes = Secao.objects.filter(area=area)

            if secoes:
                for secao in secoes:
                    secao.posts = 0
                    topicos = Topico.objects.filter(secao=secao)
                    
                    for topico in topicos:
                        posts = Post.objects.filter(topico=topico)

                        if posts:
                            secao.posts += posts.count()

                    if topicos:
                        secao.topicos = topicos

                    subsecoes = SubSecao.objects.filter(secao=secao)
                    secao.subsecoes = subsecoes
                    secao.ultimoPost = Post.objects.filter(topico__secao=secao).last()

            area.secoes = secoes
        
        context['areas'] = areas
        return self.render_to_response(context)