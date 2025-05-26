
class Usuario:
  def __init__ (self, nome:str, email:str, senha:str, cpf:str, cep:str, id_user:str):
    self.nome= nome
    self.email= email
    self.senha = senha
    self.cpf= cpf
    self.cep = cep
    self.id_user = id_user
  
  def alterar_nome(self, n_nome):
    self.nome = n_nome
    
  def alterar_email(self, n_email):
    self.email = n_email
    
  def alterar_senha(self, n_senha):
    self.senha = n_senha
    
  def alterar_cpf(self, n_cpf):
    self.cpf = n_cpf

  def alterar_cep(self, n_cep):
    self.cep = n_cep