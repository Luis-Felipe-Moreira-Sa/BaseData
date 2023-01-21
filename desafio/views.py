from django.shortcuts import render

#instalar com pip
from IPython.display import display
from desafio.models import Cliente
import pandas as pd
import pyodbc
import time
import datetime



def read_excel(request):
    var = request.POST['filename']
    data_df = pd.read_excel(var)
    data_df = data_df.sort_values(by='nascimento')
    lines_deletes = Cliente.objects.all().delete()
    save_pandas(data_df)
    # display(data_df)
    # datetoday  str(current_date())

    return render(request, 'desafio/index.html',{})


def upload_excel(request):
    return render(request, 'desafio/index.html',{})


def seconds_datetime(seconds):
    # print(seconds)
    gm =  time.gmtime(seconds)
    # print(gm)
    # DD/MM/YY H:M:S.micros
    mon = f"{gm.tm_mon}"
    if gm.tm_mon < 10:
        mon = f"0{gm.tm_mon}"
    time_data = f"{gm.tm_mday}/{mon}/{gm.tm_year}"
    # print(time_data)
    # format the string in the given format :
    # day/month/year
    format_data = '%d/%m/%Y'
    date = datetime.datetime.strptime(time_data, format_data)
    return date.date()


def save_pandas(data_df):
    # tuples = [tuple(x) for x in df.values]
    for x in data_df.values:
        x[7] = seconds_datetime(x[7])
        for a in x:
            print(type(a))
        b = Cliente(
            id_codigo = int(x[1]),
            nome = x[2],
            sobrenome = x[3],
            sexo = x[4],
            altura = x[5],
            peso = x[6],
            nascimento = x[7],
            bairro = x[8],
            cidade = x[9],
            estado = x[10],
            numero = x[11],
        )
        print(b)
        b.save()
        # print(x[7])


def all_queries(sexo):
    all_queries = list(Cliente.objects.all().filter(cidade=sexo))
    for q in all_queries:
        print(q)


# GET: retornando mulheres de mereen
def mereen():
    all_queries = Cliente.objects.all().filter(cidade='Meeren')
    print(q)
    for q in all_queries:
        print(q)


# GET: receber o sexo (m ou f) como parâmetro, filtrar e retornar a lista
# depessoas, ordenada por idade


# Create your views here

# all_queries()
# mereen()
