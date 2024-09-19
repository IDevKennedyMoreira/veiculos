# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from .models import Veiculo
# from .serializers import VeiculoSerializer
# from rest_framework.response import Response

# class VeiculoViewSet(viewsets.ModelViewSet):
#     queryset = Veiculo.objects.all()
#     serializer_class = VeiculoSerializer
#     permission_classes = [IsAuthenticated]

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         status = request.data.get('status')
#         if status in ['CONNECTADO', 'DESCONECTADO']:
#             instance.status = status
#             instance.save()
#             serializer = self.get_serializer(instance)
#             return Response(serializer.data)
#         return Response({'error': 'Status inválido'}, status=400)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Veiculo
from .serializers import VeiculoSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar veículos.
    
    Permite listar, criar, atualizar e excluir veículos.
    Apenas usuários autenticados podem acessar os endpoints.
    """
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        """
        Atualiza um veículo existente, permitindo alterar o status.
        """
        instance = self.get_object()
        
        # Verifica se o status está presente na requisição
        status_value = request.data.get('status')
        if status_value in ['CONECTADO', 'DESCONECTADO']:
            instance.status = status_value
        
        # Atualiza os demais campos usando o serializer
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)  # Valida os dados
        serializer.save()  # Salva as alterações

        return Response(serializer.data)  # Retorna os dados atualizados

    def create(self, request, *args, **kwargs):
        """
        Cria um novo veículo.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """
        Exclui um veículo existente.
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

