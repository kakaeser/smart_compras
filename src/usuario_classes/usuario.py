class Usuario:
  def __init__ (self, nome:str, email:str, senha:str, cpf:str, cep:str, id_user:str):
    self._nome= nome
    self._email= email
    self._senha = senha
    self._cpf= cpf
    self._cep = cep
    self._id_user = id_user
  
  @property
  def nome(self) -> str:
    return self._nome

  @nome.setter
  def nome(self, n_nome) -> None:
    self._nome = n_nome
    
  @property
  def email(self) -> str:
    return self._email 

  @email.setter
  def email(self, n_email) -> None:
    self._email = n_email
  
  @property
  def senha(self) -> str:
    return self._senha
    
  @senha.setter
  def senha(self, n_senha) -> None:
    self._senha = n_senha
  
  @property
  def cpf(self) -> str:
    return self._cpf
  
  @cpf.setter
  def cpf(self, n_cpf) -> None:
    self._cpf = n_cpf

  @property
  def cep(self) -> str:
    return self._cep
  
  @cep.setter
  def cep(self, n_cep) -> None:
    self._cep = n_cep

  @property
  def id_user(self) -> str:
    return self._id_user
  