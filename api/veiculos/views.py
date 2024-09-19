from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Veiculo
from .serializers import VeiculoSerializer
from rest_framework.response import Response

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        status = request.data.get('status')
        if status in ['CONNECTADO', 'DESCONECTADO']:
            instance.status = status
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({'error': 'Status inválido'}, status=400)
