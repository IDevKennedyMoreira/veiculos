from django.db import models

class Veiculo(models.Model):
    """
    Modelo que representa um veículo.

    Attributes:
        nome (str): O nome do veículo.
        modelo (str): O modelo do veículo.
        ano (int): O ano de fabricação do veículo.
        cor (str): A cor do veículo.
        status (str): O status do veículo, podendo ser
                      'CONECTADO' ou 'DESCONECTADO'.
    """
    STATUS_CHOICES = [
        ('CONECTADO', 'Conectado'),
        ('DESCONECTADO', 'Desconectado'),
    ]

    nome = models.CharField(max_length=100)  # Nome do veículo
    modelo = models.CharField(max_length=100, default="")  # Modelo do veículo
    ano = models.IntegerField(default=1800)  # Ano de fabricação do veículo
    cor = models.CharField(max_length=50, default="")  # Cor do veículo
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='DESCONECTADO')

    def __str__(self):
        """Retorna uma representação em string do veículo."""
        return f"{self.nome} ({self.modelo}, {self.ano}, {self.cor})"