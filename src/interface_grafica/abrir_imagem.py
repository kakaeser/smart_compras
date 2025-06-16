import os
from PIL import Image
from customtkinter import *

class AbrirImagens:
    def __init__(self) -> None:
        caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.caminho_icones = os.path.join(caminho_base, "..","images", "icones")
        self.caminho_supermercados = os.path.join(caminho_base, "..","images", "supermercados")
    
    def carregar_icones(self, nome_arquivo:str, tamanho: tuple[int,int]) -> CTkImage:
        caminho_completo = os.path.join(self.caminho_icones, nome_arquivo)
        imagem = Image.open(caminho_completo)
        return CTkImage(imagem, size = tamanho)
    
    def carregar_supermercados(self, nome_arquivo:str, tamanho: tuple[int,int]) -> CTkImage:
        caminho_completo = os.path.join(self.caminho_supermercados, nome_arquivo)
        imagem = Image.open(caminho_completo)
        return CTkImage(imagem, size = tamanho)