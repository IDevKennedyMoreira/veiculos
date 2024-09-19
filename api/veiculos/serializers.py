from rest_framework import serializers
from .models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Veiculo.

    Este serializador converte instâncias do modelo Veiculo
    em representações JSON e vice-versa.
    """
    
    class Meta:
        model = Veiculo
        read_only_fields = ['id']
        fields = '__all__'