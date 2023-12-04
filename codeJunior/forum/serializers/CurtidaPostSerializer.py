from rest_framework import serializers
from forum.models import CurtidaPost
from cadastro.serializers import PerfilSerializer

class CurtidaPostSerializer(serializers.ModelSerializer):
    quemCurtiu = PerfilSerializer()
    
    class Meta:
        model = CurtidaPost
        fields = '__all__'