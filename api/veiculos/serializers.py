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
        fields = '__all__'