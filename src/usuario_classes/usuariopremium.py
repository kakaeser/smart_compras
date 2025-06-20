from usuario_classes.usuario import Usuario
import math

class UsuarioPremium(Usuario):
  def __init__ (self, nome:str, email:str, senha:str, cpf:str, cep:str, id_user:str):
    super().__init__(nome, email, senha, cpf, cep, id_user)

  def calcular_novo_id(self, novo:str) -> str:
    new_id = "USR" + novo + "P"
    return new_id
  
  @Usuario.id_user.setter
  def id_user(self, idn:str) -> None:
    self.id_user = idn

  
  def calcular_distancia(self, d1:int, d2:int) -> int:
    soma2= d1**2 + d2**2
    distancia = math.sqrt(soma2)
    return distancia
