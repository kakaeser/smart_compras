from usuario_classes.usuario import Usuario
import math

class UsuarioPremium(Usuario):
  def __init__ (self, nome, email, senha, cpf, cep, id_user):
    super().__init__(nome, email, senha, cpf, cep, id_user)

  def calcular_novo_id(self, novo):
    new_id = "USR" + novo + "P"
    return new_id
  
  @Usuario.id_user.setter
  def id_user(self, idn):
    self.id_user = idn

  
  def calcular_distancia(self, d1, d2):
    soma2= d1**2 + d2**2
    distancia = math.sqrt(soma2)
    return distancia
