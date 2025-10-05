# Documentação de como usar variáveis de ambiente

## O que são

Em vários momentos usamos variáveis de ambiente para customizar a funcionalidade de uma API. Um exemplo seria ter uma váriavel "DEV_MODE" que, caso seja verdadeira, desliga mecanismos de autenticação de uma ou outra rota. Para esses casos, usamos váriaveis de ambiente, que são colocadas em um arquivo ".env" (que não é uploadado para o github!).

Com isso, conseguimos rodar o mesmo software em dois lugares diferentes, tendo comportamentos distintos.

## Problemas

Usar váriaveis de ambiente adiciona um ponto de falha no aplicativo. No nosso exemplo anterior, se "DEV_MODE" não for nem "true" nem "false", o aplicativo pode não funcionar adequadamente. Já em outros casos, temos variáveis de ambiente capazes de derrubar o servidor (por exemplo, uma váriavel de ambiente definindo o delay de envio de requisições). Outro problema recorrente é caso um dev coloque uma variável de ambiente "a mais", que de overwrite em uma variável já usada ou ocasione em comportamentos não ideais.

Então, para resolver esse problema, teriamos que tipar e validar a variável de ambiente.

## Usando variáveis de ambiente no projeto

Para tipar e validar esses dados, criamos um arquivo central, o "config.py", e fazemos toda a validação por ele. Criamos uma classe "Settings" que vai tipar as váriaveis e importa-las do .env (tomando o cuidado de ignorar variáveis não definidas no config.py), e por fim, instanciamos essa classe "Settings" com o nome de "settings".

Pelo projeto, então, usamos esse settings, e simplesmente importamos:

```python
from core.config import settings

# Isso usa uma váriavel de ambiente, definida no .env, chamada "BACKEND_URL"
print(settings.backend_url)
```