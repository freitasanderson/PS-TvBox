from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from forum.models import Post, Secao, SubSecao,Topico

class SecaoView(LoginRequiredMixin,TemplateView):
    template_name="Secao.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        secao = Secao.objects.get(id=kwargs.get('pk'))

        topicos = Topico.objects.filter(secao=secao,subsecao=None)
                    
        for topico in topicos:

            posts = Post.objects.filter(topico=topico)
            topico.indexPost = Post.objects.get(topico=topico,index=True,ativo=True)
            topico.posts = posts
            topico.ultimoPost = posts.last()
            
            if posts:
                secao.posts = posts

        if topicos:
            secao.topicos = topicos

        subsecoes = SubSecao.objects.filter(secao=secao)

        for subsecao in subsecoes:
            topicos2 = Topico.objects.filter(subsecao=subsecao)
            subsecao.topicos = topicos2

            for topico in topicos2:
                posts = Post.objects.filter(topico=topico)

                if posts:
                    subsecao.posts = posts
            subsecao.ultimoPost = Post.objects.filter(topico__subsecao=subsecao).last()

        secao.subsecoes = subsecoes

        secao.ultimoPost = Post.objects.filter(topico__secao=secao).last()

        context['secao'] = secao

        return self.render_to_response(context)