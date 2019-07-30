## Estrutura de projeto seguindo o padrão MVC em python usando o framework Flask
Modelo criado para seminário sobre organização de pastas e blueprints da disciplina de Desenvolvimento de Software II.

#### Instalando Virtualelv:
- `sudo pip3 install virtualenv`
- `mkdir NOME_DA_PASTA`
- `which python3`
- `virtualenv --python='/caminho/retornado/python3' NOME_DA_PASTA`
- `cd NOME_DA_PASTA`
- `source bin/activate`
- *Para desativar (parar) o ambiente virtual use:* `deactivate`
- *Para remover tudo que foi instalado use, **fora da pasta (usar o comando `cd ..`)**, o comando:* `rm -r NOME_DA_PASTA`
#### Copiando modelo MVC:
- `git clone https://github.com/rodrigogmartins/flask-mvc.git`
- `cd MVC`
#### Instalando dependencias:
- *Se você tiver uma versão antiga das dependencias:* `pip uninstall -r requirements.txt`
- `pip install -r requirements.txt`
*Caso queira adicionar novas dependências não instaladas basta acessar o arquivo **requirements.txt** e colocar o nome da nova dependência*

*Para instalar dependências, previamente instaladas, a pasta **requirements.txt** rode:*
- `pip freeze > requirements.txt`
*Após basta rodar os 3 comandos listados anteriormente.*
#### Rodando o o programa:
- `python runserver.py`

##### Autores:
- Rodrigo Martins,
- João Pedro Prestes,
- Luis Henrique Jacinto.
