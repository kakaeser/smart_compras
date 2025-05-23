from banco_dados.manipulador import Manipulador
import json
import os
import random


class Manipulador_User(Manipulador):

    def caminho_arquivo():
        pasta_base = os.path.dirname(__file__)
        return os.path.join(pasta_base, "..", "banco_dados", "usuarios.json")
    

    def gerar_id_aleatorio_unico():
      try:
          with open("usuarios.json", "r") as f:
              dados = json.load(f)
              ids_existentes = {usuario["id"] for usuario in dados}
      except FileNotFoundError:
          ids_existentes = set()
  
      while True:
          novo_id = random.randint(1000, 9999)
          if novo_id not in ids_existentes:
              return f"USR{novo_id}"

    @staticmethod
    def salvar_dados(nome, email, senha, cpf, cep, select):
        if select == True:
            id1 = Manipulador_User.gerar_id_aleatorio_unico() + "P"
        else:
            id1 = Manipulador_User.gerar_id_aleatorio_unico()
        novo_usuario = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "cpf": cpf,
            "cep": cep,
            "id": id1
        }

        dados_existentes = []

        caminho = Manipulador_User.caminho_arquivo()
        if os.path.exists(caminho):
            with open(caminho, "r") as arquivo:
                try:
                    dados_existentes = json.load(arquivo)
                    if not isinstance(dados_existentes, list):
                        dados_existentes = []
                except json.JSONDecodeError:
                    pass

        for usuario in dados_existentes:
            if usuario["nome"] == nome or usuario["email"] == email:
                return False  # Usuário já existe

        dados_existentes.append(novo_usuario)

        with open(caminho, "w") as arquivo:
            json.dump(dados_existentes, arquivo, indent=4)

        return True  # Sucesso

    @staticmethod
    def carregar_dados(identificador):
        caminho = Manipulador_User.caminho_arquivo()
        if os.path.exists(caminho):
            with open(caminho, "r") as arquivo:
                try:
                    dados = json.load(arquivo)
                    if isinstance(dados, list):
                        for usuario in dados:
                            if usuario["nome"] == identificador or usuario["email"] == identificador:
                                return usuario
                except json.JSONDecodeError:
                    pass
        return None
