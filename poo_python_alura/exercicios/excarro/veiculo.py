from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self,marca,modelo):
        self._marca=marca
        self._modelo=modelo
        self._ligado= False
    
    def __str__(self):
        status= "Ligado" if self._ligado else "Desligado"
        return f"{self._marca} | {self._modelo} | {status}"

    @abstractmethod
    def ligar(ABC):
        pass
    