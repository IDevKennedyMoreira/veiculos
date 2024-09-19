from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Veiculo

class VeiculoTests(APITestCase):
    """
    Testes unitários para o modelo Veiculo.

    Inclui testes para criação, listagem, atualização e exclusão de veículos.
    """

    def setUp(self):
        """
        Configura os testes.

        Cria um usuário de teste e realiza o login para
        que os testes possam acessar os endpoints.
        """
        self.url = reverse('veiculo-list')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_veiculo(self):
        """
        Testa a criação de um novo veículo.

        Verifica se a criação do veículo retorna o status HTTP 201 (Created).
        """
        response = self.client.post(self.url, {'nome': 'Carro 1'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_veiculos(self):
        """
        Testa a listagem de veículos.

        Verifica se a listagem de veículos retorna o status HTTP 200 (OK).
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_veiculo(self):
        """
        Testa a atualização de um veículo existente.

        Verifica se a atualização do veículo retorna o status HTTP 200 (OK).
        """
        veiculo = Veiculo.objects.create(nome='Carro 1')
        response = self.client.put(reverse('veiculo-detail', args=[veiculo.id]), {'status': 'CONECTADO'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_veiculo(self):
        """
        Testa a exclusão de um veículo existente.

        Verifica se a exclusão do veículo retorna o status HTTP 204 (No Content).
        """
        veiculo = Veiculo.objects.create(nome='Carro 1')
        response = self.client.delete(reverse('veiculo-detail', args=[veiculo.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
