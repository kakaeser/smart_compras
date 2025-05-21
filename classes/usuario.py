
class Usuario:
  def __init__ (self, nome, email, senha, cpf, cep):
    self.nome= nome
    self.email= email
    self.senha = senha
    self.cpf= cpf
    self.cep = cep
  
  def mostrar_dados(self):
    print(f"{self.nome} {self.email} {self.senha} {self.cpf} {self.cep}")

    
