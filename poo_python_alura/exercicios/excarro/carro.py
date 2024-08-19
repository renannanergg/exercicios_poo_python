from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo,cor,portas):
        super().__init__(marca, modelo)
        self._portas=portas
        self._cor= cor
    
    def ligar(self):
        self._ligado = True
    
    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"
        return f"{self._marca} {self._modelo} {self._cor} - Portas: {self._portas} - Status: {status}"
