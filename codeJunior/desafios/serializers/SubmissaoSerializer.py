from rest_framework import serializers
##########################
from desafios.models import Submissao


class SubmissaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submissao
        fields = ('id', 'ciclo', 'municipio', 'atividade')