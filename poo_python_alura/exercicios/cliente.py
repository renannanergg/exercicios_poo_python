class Cliente:
    clientes=[]
    def __init__(self,nome,idade=0,peso=0,nacionalidade=None):
        self.nome= nome
        self.idade= idade
        self.peso = peso
        self.nacionalidade = nacionalidade
        Cliente.clientes.append(self)
    
    def show_clients():
        for cliente in Cliente.clientes:
            print (f'Dados do cliente : {cliente.nome} | {cliente.idade} | {cliente.nacionalidade}')


renan=Cliente('Renan',24,82.5,'Brasileiro')
Cliente.show_clients()
