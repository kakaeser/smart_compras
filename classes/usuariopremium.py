from usuario import Usuario

class UsuarioPremium(Usuario):
  def __init__ (self, nome, email, senha, cpf, cep):
    super().__init__(nome, email, senha, cpf, cep, id_user)
