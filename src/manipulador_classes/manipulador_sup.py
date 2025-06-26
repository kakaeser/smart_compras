from manipulador_classes.manipulador import Manipulador
import json
import os
from typing import Optional, Dict, Any

class Manipulador_Sup(Manipulador):
    def caminho_arquivo() -> str:
        pasta_base = os.path.dirname(__file__)
    
        return os.path.join(pasta_base,".." ,"..", "banco_dados", "supermercados.json")
    
    @staticmethod
    def carregar_dados(identificador:str) -> Optional[Dict[str, Any]]:
        caminho = Manipulador_Sup.caminho_arquivo()
        if os.path.exists(caminho):
            with open(caminho, "r", encoding="utf-8") as arquivo:
                try:
                    dados = json.load(arquivo)
                    if isinstance(dados, list):
                        for supermercado in dados:
                            if supermercado["Nome"] == identificador:
                                return supermercado
                except json.JSONDecodeError:
                    pass
        return None
    @staticmethod
    def achar_nomes():
        nomes_supermercados = []
        caminho = Manipulador_Sup.caminho_arquivo()
        
        if not os.path.exists(caminho):
            print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
            return []

        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                dados_supermercados = json.load(f)
                
            if isinstance(dados_supermercados, list):
                for supermercado in dados_supermercados:
                    if isinstance(supermercado, dict) and "Nome" in supermercado:
                        nomes_supermercados.append(supermercado["Nome"])
                    else:
                        print(f"Aviso: Item inesperado no JSON ou chave 'nome' ausente: {supermercado}")
            else:
                print(f"Erro: O conteúdo do arquivo JSON não é uma lista. Tipo: {type(dados_supermercados)}")
                
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar o JSON do arquivo '{caminho}': {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
            
        return nomes_supermercados

    @staticmethod
    def editar_dados(identificador:str, campo:str, novo_valor: Any) -> bool:
        caminho = Manipulador_Sup.caminho_arquivo()
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                supermercados = json.load(f)
  
            for supermercado in supermercados:
                if supermercado["Nome"] == identificador:
                    if campo in supermercado:
                        supermercado[campo] = novo_valor
                    else:
                        print(f"Campo '{campo}' não encontrado no usuário.")
                        return False
                    break
            else:
                print("Usuário não encontrado.")
                return False
  
            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(supermercados, f, indent=4, ensure_ascii=False)
  
            return True
  
        except Exception as e:
            print("Erro ao editar usuário:", e)
            return False