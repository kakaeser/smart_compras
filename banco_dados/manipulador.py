from abc import ABC , abstractmethod
from typing import Optional, Dict, Any

class Manipulador(ABC):
    @staticmethod
    @abstractmethod
    def caminho_arquivo() -> str:
        pass
    
    @abstractmethod
    def salvar_dados() -> bool:
        pass

    @abstractmethod
    def carregar_dados() -> Optional[Dict[str, Any]]:
        pass
    @abstractmethod
    def editar_dados() -> bool:
        pass