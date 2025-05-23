from abc import ABC , abstractmethod

class Manipulador(ABC):
    @abstractmethod
    def caminho_arquivo(self):
        pass
    
    @abstractmethod
    def salvar_dados(self):
        pass

    @abstractmethod
    def carregar_dados(self):
        pass