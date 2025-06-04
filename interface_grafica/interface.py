from interface_grafica.login import Login
from interface_grafica.app import App
from interface_grafica.cadastro import Cadastro
from interface_grafica.user import User

class Interface(Login, App, Cadastro, User):
    def __init__(self):
        super().__init__("", "","")


