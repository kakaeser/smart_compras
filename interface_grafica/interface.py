from interface_grafica.login import Login
from interface_grafica.app import App
from interface_grafica.cadastro import Cadastro

class Interface(Login, App, Cadastro):
    def __init__(self):
        super().__init__("", "","")


