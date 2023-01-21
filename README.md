# Desafio Consumir Arquivo
Nesse desafio iremos avaliar suas habilidades em:
● Python
● Django
● Django REST Framework
# Descrição do projeto
Você recebeu um arquivo com dados de alguns clientes que precisam ser
importadas
para um banco de dados. Será necessária a criação de dois endpoints para que os
dados sejam consumidos. O arquivo data.xlsx está disponível para realizar os seus
testes necessários.
Sua aplicação deve:
● Ter uma tela (via um formulário) para fazer o upload do excel.
● Realizar carga de dados.
● Transformar coluna "nascimento" para data.
● Após a carga de dados você deve criar os dois endpoints abaixo usando
DRF:
● GET: retornando mulheres de mereen.
● GET: receber o sexo (m ou f) como parâmetro, filtrar e retornar a lista
de pessoas, ordenada por idade.
## Configurando o ambiente para executar a aplicação web.
Faça o download deste repositorio:

```
$ git clone git@github.com:Luis-Felipe-Moreira-Sa/BaseData.git
```

Crie um maquina virtual e instale a bibliotecas disponiveis no 
arquivo requirementes.txt:

Entre na pasta criada e inicie um ambiente virtual:
```
$ cd BaseData
$ virtualenv env
```
Depois voce deve ativa-lo com o seguinte comando:

```
$ . /env/bin/activate
```
Apos ativado, instale as bibliotecas necessárias para executar o projeto:
```
 (env)$ pip install django
 
 (env)$ pip install djangorestframework
```
Para poder ter o primeiro acesso e pode configurar o aplicação vamos executar o comando  'migrate' para gerar o banco de dados padrão do Django(SQLite).

```
(env)$ python3 manage.py migrate
```
E para ter acesso ao administrador do Django criaremos o superusuario:
```
(env)$ python3 manage.py createsuperuser
Usuário: admin
E-mail: admin@mail.com
Password: 
Password (again):
```
Para iniciar o servidor depois deste passo você deve:
```
(env)$ python3 manage.py runserver
```


Para visualizar se tudo esta executando como esperado vamos acessar o seguinte endereço pelo seu navegador de internet:
[http://localhost:8000/]

Ou você pode ter acesso a admin do Django:
[http://localhost:8000/admin]

# BaseData
# BaseData
# BaseData
