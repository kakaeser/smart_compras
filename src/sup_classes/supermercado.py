import json

class Supermercado:
    def __init__(self, dados):
        self.nome = dados["Nome"]
        self.imagem = dados["Nome imagem"]
        self.distancia_x = dados["Distância X"]
        self.distancia_y = dados["Distância Y"]
        self.produtos = {
            chave: valor for chave, valor in dados.items()
            if chave not in ["Nome", "Nome imagem", "Distância X", "Distância Y"]
        }

    def __str__(self):
        return f"{self.nome} ({self.distancia_x}, {self.distancia_y}) com {len(self.produtos)} produtos"
    



    def distancia_preco(self):
        distancia = (self.distancia_x**2 + self.distancia_y)**0.5
        return distancia


# Lê os dados do arquivo JSON
with open("supermercados.json", "r", encoding="utf-8") as f:
    dados_supermercados = json.load(f)

# Cria os objetos
supermercado1 = Supermercado(dados_supermercados[0])
supermercado2 = Supermercado(dados_supermercados[1])
supermercado3 = Supermercado(dados_supermercados[2])
supermercado3 = Supermercado(dados_supermercados[3])
supermercado4 = Supermercado(dados_supermercados[4])
supermercado5 = Supermercado(dados_supermercados[5])
supermercado6 = Supermercado(dados_supermercados[6])
supermercado7 = Supermercado(dados_supermercados[7])
supermercado8 = Supermercado(dados_supermercados[8])
supermercado9 = Supermercado(dados_supermercados[9])
supermercado10 = Supermercado(dados_supermercados[10]) 
supermercado11 = Supermercado(dados_supermercados[11])
supermercado12 = Supermercado(dados_supermercados[12])
supermercado13 = Supermercado(dados_supermercados[13])
supermercado14 = Supermercado(dados_supermercados[14])
supermercado15 = Supermercado(dados_supermercados[15])
supermercado16 = Supermercado(dados_supermercados[16])
supermercado17 = Supermercado(dados_supermercados[17])
supermercado18 = Supermercado(dados_supermercados[18])
supermercado19 = Supermercado(dados_supermercados[19])


# Exemplo de uso
print(supermercado1)
print(supermercado2)
print(supermercado19)

# Preço de um produto específico
produto = "Coca-Cola"
print(f"\nPreço da {produto}:")
print(f"{supermercado1.nome}: R$ {supermercado1.produtos[produto]}")
print(f"{supermercado2.nome}: R$ {supermercado2.produtos[produto]}")
