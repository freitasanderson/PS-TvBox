from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from cadastro.models import Perfil
from forum.models import Topico, Post, RespostaPost
from forum.forms import PostForm
class TopicoView(LoginRequiredMixin, DetailView):
    model = Topico
    template_name = "Topico.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.object = self.get_object()

        posts = Post.objects.filter(topico=self.object,ativo=True).order_by('-index','dataCadastro')
        for post in posts:
            post.curtido = post.curtidapost_set.filter(quemCurtiu__pessoa__user=self.request.user,ativo=True).exists()
            post.curtidas = post.curtidapost_set.filter(ativo=True)
            
            if post.resposta.filter(resposta=post, ativo=True).exists():
                post.respondendo = RespostaPost.objects.get(resposta=post)

        context['topico'] = self.object
        context['pessoaPerfil'] = Perfil.objects.get(pessoa__user=self.request.user)
        context['form'] = PostForm()
        context['posts'] = posts

        # print(f'Context: {context}')

        return context
