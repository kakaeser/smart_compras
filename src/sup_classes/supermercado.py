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

    def preco_final(self, lista_compras : tuple[str, int]): 
        
        soma = 0
        for produto_nome, foi_selecionado in lista_compras.items():
                if foi_selecionado == 1:
                     soma = soma + self.produtos[produto_nome]
                     
        return soma
