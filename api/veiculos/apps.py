from django.apps import AppConfig

class VeiculosConfig(AppConfig):
    """
    Configuração do aplicativo 'veiculos'.

    Esta classe define as configurações específicas para o aplicativo,
    como o nome do aplicativo e o tipo de campo de ID padrão.
    """
    
    default_auto_field = 'django.db.models.BigAutoField'  # Define o tipo de campo padrão para IDs como BigAutoField
    name = 'veiculos'  # Nome do aplicativo