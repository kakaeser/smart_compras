
class Usuario:
  def __init__ (self, nome:str, email:str, senha:str, cpf:str, cep:str, id_user:str):
    self.nome= nome
    self.email= email
    self.senha = senha
    self.cpf= cpf
    self.cep = cep
    self.id_user = id_user
  
  def mostrar_dados(self):
    print(f"{self.nome} {self.email} {self.senha} {self.cpf} {self.cep} {self.id_user}")

    
