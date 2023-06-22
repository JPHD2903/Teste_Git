 #framework que permitem criar sites e api's no python 
import pandas as pd #lê nossa base de dados

livros = [
    {   
        'id': 1,
        'título': 'O nome do Vento',
        'valor': 50
    },
    {   
        'id': 2,
        'título': 'A sutil arte do fodasse',
        'valor': 12
    },
    {   
        'id': 3,
        'título': 'Harry Potter',
        'valor': 34
    }
]

tabela = pd.read_csv(livros)
total_valor = tabela['valor'].sum()
print(total_valor)