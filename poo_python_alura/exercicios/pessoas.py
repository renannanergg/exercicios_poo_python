from datetime import datetime
class Pessoa:

    def __init__(self,nome='',idade=0,profissao=''):
        self._nome=nome.title()
        self._idade = idade
        self._profissao = profissao.title()

    def __str__(self):
        return f' {self._nome} | {self._idade} | {self._profissao}'
    
    def aniversario(self):
        self._idade + 1
    
    @property
    def saudacao(self):
        if self._profissao:
            print(f'Muito prazer, me chamo {self._nome} e sou {self._profissao}')
        else:
            print(f'Saudações ! meu nome é {self._nome}')

# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=28, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=31, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=20)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)