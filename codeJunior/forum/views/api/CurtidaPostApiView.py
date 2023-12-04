from rest_framework import viewsets
from rest_framework.response import Response

from forum.models import Post, CurtidaPost
from cadastro.models import Perfil
import json

from forum.serializers import CurtidaPostSerializer

class CurtidaPostApiView(viewsets.ViewSet):
    
    def create(self, request, *args, **kwargs):
        # print(f'Request: {request.POST}')

        post = Post.objects.get(id=request.POST.get('post'))
        
        try:
            quemCurtiu = Perfil.objects.get(pessoa__user__username = request.user)
        except:
            quemCurtiu = None
        
        if not quemCurtiu:
            responseData = {'mensagem': 'Não autorizado'}
            status=203   
            return Response(responseData,status=status)

        temCurtida = CurtidaPost.objects.filter(post=post,quemCurtiu=quemCurtiu).exists()

        if temCurtida:
            curtida = CurtidaPost.objects.get(post=post,quemCurtiu=quemCurtiu)
            curtida.ativo = True if curtida.ativo == False else False
            curtida.save()
        
        else:
            curtida = CurtidaPost()
            curtida.post = post
            curtida.quemCurtiu = quemCurtiu
            curtida.save()

        curtidas = CurtidaPost.objects.filter(post=post,ativo=True)
        curtidas_serialized = CurtidaPostSerializer(curtidas, many=True)

        responseData = {'status': curtida.ativo,
                        'curtidas': curtidas_serialized.data,
                    }
        status=201  

        return Response(responseData,status=status)