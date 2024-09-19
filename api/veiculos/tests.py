from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Veiculo
from rest_framework.authtoken.models import Token

class VeiculoAPITests(APITestCase):
    """
    Testes para o modelo Veiculo utilizando o Django Rest Framework.
    Inclui criação, listagem, atualização e exclusão de veículos.
    """
    def setUp(self):
        """
        Configura o ambiente de teste criando um usuário e gerando um token de autenticação.
        """
        # Cria um usuário para autenticação
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Gera um token para o usuário
        token = Token.objects.create(user=self.user)
        # Adiciona o token no cabeçalho das requisições
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        # URL da listagem de veículos
        self.url = reverse('veiculo-list')

    def test_create_veiculo(self):
        """
        Testa a criação de um novo veículo.
        Verifica se o veículo é criado corretamente.
        """
        data = {
            'nome': 'Carro Teste',
            'modelo': 'Modelo X',
            'ano': 2020,
            'cor': 'Vermelho',
            'status': 'CONECTADO'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Veiculo.objects.count(), 1)
        veiculo = Veiculo.objects.get()
        self.assertEqual(veiculo.nome, 'Carro Teste')
        self.assertEqual(veiculo.modelo, 'Modelo X')
        self.assertEqual(veiculo.ano, 2020)
        self.assertEqual(veiculo.cor, 'Vermelho')
        self.assertEqual(veiculo.status, 'CONECTADO')

    def test_list_veiculos(self):
        """
        Testa a listagem de veículos.
        Verifica se todos os veículos são retornados corretamente.
        """
        Veiculo.objects.create(nome='Carro 1', modelo='Modelo A', ano=2019, cor='Azul', status='CONECTADO')
        Veiculo.objects.create(nome='Carro 2', modelo='Modelo B', ano=2021, cor='Preto', status='DESCONECTADO')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['nome'], 'Carro 1')
        self.assertEqual(response.data[1]['nome'], 'Carro 2')


    def test_update_veiculo(self):
        """
        Testa a atualização de um veículo existente.
        Verifica se os dados do veículo são atualizados corretamente.
        """
        # Cria um veículo para o teste
        veiculo = Veiculo.objects.create(nome='Carro 1', modelo='Modelo A', ano=2019, cor='Azul', status='CONECTADO')

        # Dados que serão usados para atualizar o veículo
        data = {
            'nome': 'Carro Atualizado',
            'modelo': 'Modelo C',
            'ano': 2022,
            'cor': 'Branco',
            'status': 'DESCONECTADO'
        }

        # Realiza a requisição PUT para atualizar o veículo
        response = self.client.put(reverse('veiculo-detail', args=[veiculo.id]), data, format='json')

        # Verifica se o status da resposta é 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Atualiza o objeto veiculo com os novos dados do banco de dados
        veiculo.refresh_from_db()

        # Verifica se os dados foram atualizados corretamente
        self.assertEqual(veiculo.nome, 'Carro Atualizado')
        self.assertEqual(veiculo.modelo, 'Modelo C')
        self.assertEqual(veiculo.ano, 2022)
        self.assertEqual(veiculo.cor, 'Branco')
        self.assertEqual(veiculo.status, 'DESCONECTADO')

    # def test_update_veiculo(self):
    #     """
    #     Testa a atualização de um veículo existente.
    #     Verifica se os dados do veículo são atualizados corretamente.
    #     """
    #     veiculo = Veiculo.objects.create(nome='Carro 1', modelo='Modelo A', ano=2019, cor='Azul', status='CONECTADO')
    #     data = {
    #         'nome': 'Carro Atualizado',
    #         'modelo': 'Modelo C',
    #         'ano': 2022,
    #         'cor': 'Branco',
    #         'status': 'DESCONECTADO'
    #     }

    #     response = self.client.put(reverse('veiculo-detail', args=[veiculo.id]), data)
    #     print(response)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     veiculo.refresh_from_db()
    #     self.assertEqual(veiculo.nome, 'Carro Atualizado')
    #     self.assertEqual(veiculo.modelo, 'Modelo C')
    #     self.assertEqual(veiculo.ano, 2022)
    #     self.assertEqual(veiculo.cor, 'Branco')
    #     self.assertEqual(veiculo.status, 'DESCONECTADO')

    def test_delete_veiculo(self):
        """
        Testa a exclusão de um veículo existente.
        Verifica se o veículo é removido corretamente.
        """
        veiculo = Veiculo.objects.create(nome='Carro 1', modelo='Modelo A', ano=2019, cor='Azul', status='CONECTADO')

        response = self.client.delete(reverse('veiculo-detail', args=[veiculo.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Veiculo.objects.count(), 0)
