import json
from classes import Supermercado

with open ('supermercados.json', 'r') as arquivo:
    lista_dados = json.load(arquivo)

lista_supermercados = []

for dados in lista_dados:
    supermercado = Supermercado(dados['nome'], dados['idade'], dados['cidade'])
    lista_supermercados.append(supermercado)

# Imprimir todos os objetos criados
for pessoa in lista_de_pessoas:
    print(pessoa)