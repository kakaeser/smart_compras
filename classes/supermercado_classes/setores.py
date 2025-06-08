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


#Classes dentro de Setores: Limpeza, Hortifruti, Lacticinios, HigienePessoal, Açougue, Bebidas, Padaria, Biscoitos
class Limpeza:
    def __init__(self, produtos):
        self.produtos = []

    def add_produto(self, produto):
        self.produtos.append(produto)
        
class Hortifruti:
    def __init__(self, produtos):
        self.produtos = []

    def add_produto(self, produto):
        self.produtos.append(produto)
        
class Lacticinios:
    def __init__(self, produtos):
        self.produtos = []

    def add_produto(self, produto):
        self.produtos.append(produto)
        
class HigienePessoal:
    def __init__(self, produtos):
        self.produtos = []

    def add_produto(self, produto):
        self.produtos.append(produto)
        
class Açougue:
    def __init__(self, produtos):
        self.produtos = []

    def add_produto(self, produto):
        self.produtos.append(produto)
        
class Bebidas:
    def __init__(self, produtos):
        self.produtos = []

    def add_produto(self, produto):
        self.produtos.append(produto)

class Padaria:
    def __init__(self, produtos):
        self.produtos = []

    def add_produto(self, produto):
        self.produtos.append(produto)

class Biscoitos:
    def __init__(self, produtos):
        self.produtos = []

    def add_produto(self, produto):
        self.produtos.append(produto)
        


