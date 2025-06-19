from customtkinter import *
from PIL import Image
from interface_grafica.login import Login
from interface_grafica.app import App
from interface_grafica.cadastro import Cadastro
from interface_grafica.user import User
from interface_grafica.cards import Cards
from interface_grafica.lista import Lista
from interface_grafica.abrir_imagem import AbrirImagens
from interface_grafica.pagamento import Pagamento

class Interface(Login, App, Cadastro, User, Cards, Lista, AbrirImagens, Pagamento):
    def __init__(self):
        Login.__init__(self,"", "","")
        Cards.__init__(self)
        Lista.__init__(self)
        AbrirImagens.__init__(self)
        App.__init__(self)
        Cadastro.__init__(self)


