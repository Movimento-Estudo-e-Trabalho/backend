"""
Configuration Settings Module

Esse modulo define as configurações da aplicação usando o "BaseSettings" do Pydantic.
É um lugar central para configurar e carregar váriaveis de ambiente
de um .env file or system environment.

Uso:
    from core.config import settings

    # Acesse variaveis de ambiente assim:
    backend_url = settings.backend_url

    Environment Variables:
    Qualquer setting (minusculo) pode ser sobrescrita com uma variável de ambiente de mesmo nome (maiuscula).
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings class for the application,
    for the documentation of the settings, see the README.md file

    The settings are loaded from the .env file,
    the environment variables will override the settings when a value with the same name is set
    the environment variables must be in uppercase,
    for example: OPENAI_API_KEY on the .env file defines the openai_api_key setting
    """

    # URL em que essa aplicação está deployada
    backend_url: str = ""

    # Configurações Postgres
    postgres_user: str = ""
    postgres_password: str = ""
    postgres_host: str = ""
    postgres_port: str = ""
    postgres_db: str = ""

    # URL em que o frontend correspondente está deployado
    frontend_url: str = ""

    class Config:
        # Essa configuração carrega "settings" do env se elas existirem
        env_file = ".env"
        extra = "ignore"  # Ignore variáveis do .env que não estejam definidas aqui


# Criando uma instância global do settings que vai ser importada pela aplicação para interagir com as váriaveis de ambiente
settings = Settings()
