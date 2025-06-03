from abc import ABC , abstractmethod
from typing import Optional, Dict, Any

class Manipulador(ABC):
    @staticmethod
    @abstractmethod
    def caminho_arquivo() -> str:
        pass
    
    @abstractmethod
    def salvar_dados(nome:str, email:str, senha:str, cpf:str, cep:str, select:bool) -> bool:
        pass

    @abstractmethod
    def carregar_dados(identificador:str) -> Optional[Dict[str, Any]]:
        pass
    @abstractmethod
    def editar_dados(identificador:str, campo:str, novo_valor: Any) -> bool:
        pass