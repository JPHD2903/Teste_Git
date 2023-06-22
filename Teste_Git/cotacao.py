import requests 
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
#Aqui eu estou pegando o link e filtrando para mostrar somente oque eu quero 
#cotacao_dolar = cotacoes['USDBRL']["bid"]
print(cotacoes)
#print("A cotação do dólar é:", cotacao_dolar)
