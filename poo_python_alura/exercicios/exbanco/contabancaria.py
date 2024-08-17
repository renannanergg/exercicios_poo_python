class ContaBancaria:
    def __init__(self,titular='',saldo=0,segmento=''):
        self.titular=titular.title()
        self.saldo=saldo
        self._segmento=segmento
        self._ativo= False
    
    def __str__(self):
        return f'Titular: {self.titular}| {self._segmento} | Status: {self.ativo}| Saldo: R${self.saldo}'
    
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    @classmethod
    def ativar_conta(cls,self):
        self._ativo = True
    

