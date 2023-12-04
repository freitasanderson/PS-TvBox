import subprocess

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from desafios.models import Submissao, Desafio
from cadastro.models import Pessoa

import json


class SubmissaoCreateViewSet(APIView):
    # serializer_class = SubmissaoSerializer
    queryset = Submissao.objects.all()

    def executarCodigo(self, codigo):
        try:
            resultadoBytes = subprocess.check_output(['python', '-c', codigo], stderr=subprocess.STDOUT, timeout=10)
            resultadoStr = resultadoBytes.decode('utf-8')
            
            return resultadoStr
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')
        except subprocess.TimeoutExpired:
            return "Tempo limite excedido."

    def post(self, request, pk):
        desafioPk = request.data.get('problema')
        pessoa = request.data.get('pessoa')
        codigo = request.data.get('codigo')

        print(request.data)

        desafio = Desafio.objects.get(pk=desafioPk)
        resultadoUsuario = self.executarCodigo(codigo)

        solucoes = list()
        temSolucaoCorreta = 0

        for solucao in desafio.solucao_set.all():
            objSolucao = dict()
            objSolucao["desafio"] = solucao.desafio.titulo
            objSolucao["entrada"] = solucao.entrada
            objSolucao["secreta"] = solucao.secreta

            if resultadoUsuario.strip() == str(solucao.entrada).strip():
                objSolucao["correta"] = True
                temSolucaoCorreta = temSolucaoCorreta + 1
            else:
                objSolucao["correta"] = False
            
            solucoes.append(objSolucao)
                
        
        submissao = Submissao()
    
        submissao.pessoa = Pessoa.objects.get(user__pk=pessoa)
        submissao.codigo = codigo
        submissao.problema = desafio

        if temSolucaoCorreta > 0:
            submissao.resultado = 1
        else:
            submissao.resultado = 0

        submissao.save()
        print(solucoes)
        data = json.dumps(solucoes, ensure_ascii=False) 
        print(data)
        return Response(data, status=status.HTTP_200_OK)
