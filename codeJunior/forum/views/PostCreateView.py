from django.conf import settings
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
##########
from forum.models import Topico, Post,RespostaPost
from forum.forms import PostForm

class PostCreateView(UpdateView):
    form_class = PostForm
    model = Post
    mensagemSucesso = 'Post criado com sucesso'
    mensagemError = 'Não foi possível criar o post'

    def post(self, request, *args, **kwargs):
        # print(f'Request: {request.POST}')
        form = self.get_form()
        # print(f'Form: {form}')

        if form.is_valid():
            post = form.save(commit=False)
            post.id = None
            post.ativo = True
                
            post.save()
            if request.POST.get('respondendo'):
                resposta = RespostaPost()
                resposta.post = Post.objects.get(id=request.POST.get('respondendo'))
                resposta.resposta = post
                resposta.ativo = True
                resposta.save()
            

            messages.success(self.request, self.mensagemSucesso)
            return HttpResponseRedirect(reverse('forum:topicoView',  kwargs={'pk': post.topico.id}))
        else:
            return self.form_invalid(form)
        