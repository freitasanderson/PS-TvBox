from django.shortcuts import render
from django.views.generic import TemplateView

from forum.models import Post, Secao, SubSecao,Topico

class SubsecaoView(TemplateView):
    template_name="Subsecao.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        subsecao = SubSecao.objects.get(id=kwargs.get('pk'))

        topicos = Topico.objects.filter(subsecao=subsecao)
                    
        for topico in topicos:

            posts = Post.objects.filter(topico=topico)
            topico.indexPost = Post.objects.get(topico=topico,index=True,ativo=True)
            topico.posts = posts
            topico.ultimoPost = posts.last()
            
            if posts:
                subsecao.posts = posts

        if topicos:
            subsecao.topicos = topicos

        context['subsecao'] = subsecao

        return self.render_to_response(context)