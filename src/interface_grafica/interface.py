from customtkinter import *
from PIL import Image
from src.interface_grafica.login import Login
from src.interface_grafica.app import App
from src.interface_grafica.cadastro import Cadastro
from src.interface_grafica.user import User
from src.interface_grafica.cards import Cards
from src.interface_grafica.lista import Lista

class Interface(Login, App, Cadastro, User, Cards, Lista):
    def __init__(self):
        Login.__init__(self,"", "","")
        Cards.__init__(self)
        Lista.__init__(self)
        #iniciação das imagens
        self.logo = CTkImage(Image.open("banco_dados/imagens/icones/logo.png"), size =(128,128))
        self.user = CTkImage(Image.open("banco_dados/imagens/icones/usuario.png"), size = (32,32))
        self.config = CTkImage(Image.open("banco_dados/imagens/icones/config.png"), size = (32,32))
        self.menu = CTkImage(Image.open("banco_dados/imagens/icones/menu.png"), size = (32,32))
        self.tema = CTkImage(Image.open("banco_dados/imagens/icones/tema.png"), size = (16,16))
        self.fechar = CTkImage(Image.open("banco_dados/imagens/icones/fechar.png"), size = (16,16))
        self.sair = CTkImage(Image.open("banco_dados/imagens/icones/logout.png"), size = (16,16))
        self.premium = CTkImage(Image.open("banco_dados/imagens/icones/premium.png"), size = (16,16))
        self.busca = CTkImage(Image.open("banco_dados/imagens/icones/busca.png"), size = (16,16))
        self.busca_fail = CTkImage(Image.open("banco_dados/imagens/icones/busca_fail.png"), size = (48,48))
        self.nova_lista = CTkImage(Image.open("banco_dados/imagens/icones/nova_lista.png"), size = (16,16))
        self.selected1 = CTkImage(Image.open("banco_dados/imagens/icones/selected.png"), size = (32,32))
        self.not_selected1 = CTkImage(Image.open("banco_dados/imagens/icones/not_selected1.png"), size = (32,32))
        self.lista = CTkImage(Image.open("banco_dados/imagens/icones/lista.png"), size = (16,16))
        self.market = CTkImage(Image.open("banco_dados/imagens/supermercados/market.png"), size = (192,144))
        self.selected2 = CTkImage(Image.open("banco_dados/imagens/icones/selected.png"), size = (16,16))
        self.not_selected2 = CTkImage(Image.open("banco_dados/imagens/icones/not_selected2.png"), size = (16,16))
        self.edit = CTkImage(Image.open("banco_dados/imagens/icones/editar.png"), size = (16,16))
        self.verificar = CTkImage(Image.open("banco_dados/imagens/icones/verificar.png"), size = (16,16))


