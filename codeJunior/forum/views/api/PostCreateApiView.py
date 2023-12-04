from rest_framework import viewsets
from rest_framework.response import Response

from forum.models import Topico, Post, Secao, SubSecao
from cadastro.models import Perfil

class PostCreateApiView(viewsets.ViewSet):
    
    def create(self, request, *args, **kwargs):
        # print(f'Request: {request.POST}')

        secao = Secao.objects.get(id=request.POST.get('secao'))

        if request.POST.get('subsecao'):
            subsecao = SubSecao.objects.get(id=request.POST.get('subsecao'))
        else:
            subsecao = None

        if not request.POST.get('conteudo') or not request.POST.get('titulo') :
            responseData = {'mensagem': 'Nenhum Conteúdo'}
            status=204   
            return Response(responseData,status=status)
        try:
            quemPostou = Perfil.objects.get(pessoa__user__username = request.user)
        except:
            quemPostou = None
        
        if not quemPostou:
            responseData = {'mensagem': 'Não autorizado'}
            status=203   
            return Response(responseData,status=status)

        novoPost = Post()
        novoPost.topico = novoTopico
        novoPost.quemPostou = quemPostou
        novoPost.conteudo = request.POST.get('conteudo')
        novoPost.index = True
        novoPost.save()

        responseData = {'mensagem': 'Topico Criado!',
                        'id':novoTopico.id,
                    }
        status=201  

        return Response(responseData,status=status)