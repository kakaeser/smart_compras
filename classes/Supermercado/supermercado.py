from endereço import Endereço
from setores import *


# Na classe supermercado, preciso de: nome supermercado, endereço supermercado, produtos setorizados

class Supermercado:
    def __init__ (self, nome, endereço, setores):
        self.nome = nome
        self.endereço = endereço
        self.setores = setores
        

def publicar_dados(supermercado):
    print (supermercado.nome)
    print (supermercado.setores.limpeza.produtos)
     






