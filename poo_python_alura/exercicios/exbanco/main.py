from agencia import Agencia
from banco import Banco
from contabancaria import ContaBancaria

# Instanciando Clientes
elias=ContaBancaria(titular='Elias Mendes',saldo=2500,segmento='Gold')
jasmin=ContaBancaria(titular='Jasmin Sanchez',saldo=800,segmento='Standard')
paula=ContaBancaria(titular='Paula Pelloti',saldo=14500,segmento='Private')

clientes=[elias,jasmin,paula]

# Instanciando Banco e Agencias
Bradesco=Banco(nome='Bradesco',endereco='Cidade de Deus/Osasco')
AgenciaBradescoPrivate= Agencia(nome='Bradesco Private',endereco='Cidade de Deus/Osasco',numero=5000)
AgenciaBradescoGold= Agencia(nome='Bradesco Gold',endereco='Av. Paulista',numero=2000)
AgenciaBradescoStandard=Agencia(nome='Bradesco Standard',endereco='Av. Mutinga',numero=1200)

agencias=[AgenciaBradescoStandard,AgenciaBradescoPrivate,AgenciaBradescoGold]

# Classificando clientes de acordo com segmento
for cliente in clientes:
    if cliente._segmento == 'Private':
        print(f'{cliente} |Correntista: {AgenciaBradescoPrivate}'.ljust(25))
    elif cliente._segmento == 'Gold':
        print(f'{cliente} |Correntista: {AgenciaBradescoGold}'.ljust(25))
    else:
        print(f'{cliente} |Correntista: {AgenciaBradescoStandard}'.ljust(25))
        
