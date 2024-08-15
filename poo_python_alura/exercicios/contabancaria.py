class ContaBancaria:
    def __init__(self,titular='',saldo=0):
        self.titular=titular.title()
        self.saldo=saldo
        self._ativo= False
    
    def __str__(self):
        return f'Titular: {self.titular} | Status: {self.ativo}| Saldo: R${self.saldo}'
    
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    @classmethod
    def ativar_conta(cls,self):
        self._ativo = True
    
elias=ContaBancaria(titular='Elias Mendes',saldo=2500)
jasmin=ContaBancaria(titular='Jasmin Sanchez',saldo=800)
paula=ContaBancaria(titular='Paula Pelloti',saldo=14500)

print(elias)
print(jasmin)
print(paula)

class ClienteBanco:
    def __init__(self,nome='',conta=0,saldo=0,segmento=''):
        self._ativo=False
        self.nome= nome
        self.conta=conta
        self.saldo=saldo
        self.segmento= segmento
    
    def __str__(self):
        return f'titular: {self.nome} | saldo: R${self.saldo} | segmento : {self.segmento}'
    
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

joao=ClienteBanco(nome='João Pedro',conta=19392,saldo=580,segmento='Standard')
print(joao)
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")