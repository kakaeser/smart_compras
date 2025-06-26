class Supermercado:
    def __init__ (self, nome, obj_endereço, obj_setores):
        self.nome = nome
        self.obj_endereço = obj_endereço
        self.obj_setores = obj_setores


class Setores:
    def __init__(self, limpeza, hortifruti, lacticinios, higienepessoal, açougue, bebidas, padaria, biscoitos):
        self.limpeza = limpeza
        self.hortifruti = hortifruti
        self.lacticinios = lacticinios
        self.higienPessoal = higienepessoal
        self.açougue = açougue
        self.bebidas = bebidas
        self.padaria = padaria
        self.biscoitos = biscoitos

#classes Subsetores

class Limpeza:
    def __init__(self, produtos):
        self.produtos = []
        
class Hortifruti:
    def __init__(self, produtos):
        self.produtos = []
        
class Lacticinios:
    def __init__(self, produtos):
        self.produtos = []
        
class HigienePessoal:
    def __init__(self, produtos):
        self.produtos = []
        
class Açougue:
    def __init__(self, produtos):
        self.produtos = []
        
class Bebidas:
    def __init__(self, produtos):
        self.produtos = []

class Padaria:
    def __init__(self, produtos):
        self.produtos = []

class Biscoitos:
    def __init__(self, produtos):
        self.produtos = []
        


