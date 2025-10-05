# Leia-me

Antes de rodar o projeto, você precisará de alguns pré-requisitos:
- Python >= 3.11
- git

## Configurando o projeto no Linux
Se você utiliza um sistema Linux, o python já vem instalado por padrão, basta instalar o gerenciador de ambiente virtual. Em algumas distros (como no Fedora e no Arch) esse gerenciador já vem por padrão, mas, se você utiliza **Debian**/**Ubuntu** e derivados, precisará do pacote específico.

~~~ bash
sudo apt update # Atualizando a lista de pacotes
sudo apt install python3-venv
~~~

## Preparação
No linux, além do git eu recomendo fortemente instalar um pacote chamado *seahorse*, que vai permitir o gerenciamento gráfico das nossas chaves *SSH* (falarei disso mais adiante). 

Os comandos abaixo instalam tanto o **git** quanto o **seahorse** no seu sistema:

#### Ubuntu
~~~ bash
sudo apt install git seahorse
~~~

#### Fedora
~~~ bash
sudo dnf install git seahorse
~~~

#### ArchLinux
~~~ bash
sudo pacman -S git seahorse
~~~

Após instalados esses pacotes, você perceberá que um novo programa vai aparecer no seu *menu de aplicativos*. Ele pode se chamar **Passwords and keys** ou **Senhas e chaves** dependendo do idioma configurado.

## Criando uma nova chave via interface gráfica
Ao abrir o programa senhas e chaves, vamos adicionar uma nova chave de ssh clicando no botão **+** superior direito e selecionando a opção **chave de ssh**

![iniciando a criacao da chave](static/images/tutorial/iniciando_criacao_da_chave_ssh.png)

Após isso, precisamos definir uma descrição para a nossa chave. Também podemos alterar o tipo de chave e a força da chave, mas para nosso exemplo o padrão será suficiente.

![gerando a chave](static/images/tutorial/salvando_chave_ssh.png)

Será solicitado uma senha para a chave, e uma confirmação da mesma logo em seguida. Após isso, podemos conferir se tudo deu certo se nossa chave criada aparecer na tela inicial.

![mostrando a chave criada na tela inicial](static/images/tutorial/demonstrando_chave_ssh_criada.png)

## inserindo a chave no github

Antes de clonar o repositório na nossa máquina é nescessário adicionar a chave que criamos no github. Para isso, vamos clicar na chave e em seguida clicar no botão de copiar

![copiando chave ssh](static/images/tutorial/copiando_chave_ssh.png)

Agora, para adicionarmos a chave no github acessamos o link https://github.com/settings/keys e clicamos no botão "New SSH key"

![adicionando nova chave no github](static/images/tutorial/adicionando_nova_chave_github.png)

Na próxima tela, adicionamos uma descriçao para nossa chave e colamos a chave copiada no campo "Key"

![colando chave no github](static/images/tutorial/colando_chave_github.png)

Por fim, podemos ver nossa nova chave na próxima tela

![demonstrando a chave no github](static/images/tutorial/demonstrando_chave_adicionada_github.png)

## Clonando o repositório na máquina local

Agora, podemos clonar o [repositório remoto](https://github.com/Movimento-Estudo-e-Trabalho/backend) para nossa máquina através do github clicando no botão "Code" e copiando o link presente na aba "SSH"

![copiando link ssh](static/images/tutorial/copiando_link_ssh.png)

Finalmente, podemos abrir a pasta onde desejamos clonar o repositório pelo terminal com o comando

~~~ sh
cd /caminho/da/pasta/ # Substitua pelo caminho desejado

git clone git@github.com:Movimento-Estudo-e-Trabalho/backend.git
~~~

A pasta "Backend" aparecerá no seu gerenciador de arquivos.

## TODO Configurando o projeto no Windows

...


# Rodando o Projeto

Abrimos um terminal dentro da pasta onde clonamos o repositório

~~~ sh
cd /pasta/onde/o/repositorio/foi/clonado
~~~

e seguimos os passos abaixo:

1 - Criar um ambiente virtual

~~~ bash
python3 -m venv .venv
~~~

2 - Ativar o ambiente

~~~ bash
source .venv/bin/activate
~~~

3 - Instalar as dependências
~~~ bash
pip install -r requirements.txt
~~~

4 - Rodar o projeto
~~~
fastapi dev main.py
~~~