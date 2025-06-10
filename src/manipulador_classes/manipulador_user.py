from src.manipulador_classes.manipulador import Manipulador
import json
import os
import random
from typing import Optional, Dict, Any


class Manipulador_User(Manipulador):

    def caminho_arquivo() -> str:
        pasta_base = os.path.dirname(__file__)
        return os.path.join(pasta_base,".." ,"..", "banco_dados", "usuarios.json")
    

    def gerar_id_aleatorio_unico() -> str:
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
    def salvar_dados(nome:str, email:str, senha:str, cpf:str, cep:str, select:bool) -> bool:
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
    def carregar_dados(identificador) -> Optional[Dict[str, Any]]:
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
        
    @staticmethod  
    def editar_dados(identificador:str, campo:str, novo_valor: Any) -> bool:
        caminho = Manipulador_User.caminho_arquivo()
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                usuarios = json.load(f)
  
            for usuario in usuarios:
                if usuario["email"] == identificador or usuario["nome"] == identificador:
                    if campo in usuario:
                        usuario[campo] = novo_valor
                    else:
                        print(f"Campo '{campo}' não encontrado no usuário.")
                        return False
                    break
            else:
                print("Usuário não encontrado.")
                return False
  
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(usuarios, f, indent=4, ensure_ascii=False)
  
            return True
  
        except Exception as e:
            print("Erro ao editar usuário:", e)
            return False
        
    @staticmethod
    def conferir_dados(identificador) -> int:
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
            if usuario["nome"] == identificador:
                return 1  # Nome já existe
            elif usuario["email"] == identificador:
                return 2 # Email já existe
            elif usuario["cpf"] == identificador:
                return 3 # Email já existe
            elif usuario["id"] == identificador:
                return 4 # Email já existe
        
        return 0 # Funcionou