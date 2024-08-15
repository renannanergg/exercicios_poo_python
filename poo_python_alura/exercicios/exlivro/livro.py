class Livro:
    livros=[]

    def __init__(self, titulo='', autor='', ano_publicacao=0):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"Livro: {self._titulo} | Autor: {self._autor} | Publicado em: {self._ano_publicacao} | {self._disponivel}"
    
    @property
    def titulo(self):
        return self._titulo
    def autor(self):
        return self._autor
    def ano_publicacao(self):
        return self._ano_publicacao
    
    @classmethod
    def listar_livros(cls):
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(25)} | {livro._autor.ljust(25)} | {str(livro._ano_publicacao).ljust(25)} | {livro._disponivel}')
    
    def emprestar(self):
        self._disponivel = False
    
    @classmethod
    def verificar_disponibilidade(cls):
        ano_procurado = input('Olá. Qual o ano do livro que você busca para alugar?')
        for livro in cls.livros:
            if livro._ano_publicacao == int(ano_procurado) and livro._disponivel==True:
                print (f'O Livro {livro._titulo} do autor {livro._autor} está disponível!')
            else: print ('infelizmente não há nenhum livro disponível no momento')   

