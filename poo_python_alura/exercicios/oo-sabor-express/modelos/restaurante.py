from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    '''Representa um restaurante e suas características.'''

    restaurantes = []

    def __init__(self,nome,categoria,especialidade):
       """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
       self._nome= nome.title()
       self._categoria = categoria.upper()
       self.especialidade = especialidade
       self._avaliacao = []
       self._cardapio = []
       self._ativo = False
       Restaurante.restaurantes.append(self)
    
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome}  |  {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
         """Exibe uma lista formatada de todos os restaurantes."""
         print(f'{'Nome do Restaurante '.ljust(25)} | {'Categoria'.ljust(25)} | {'Especialidade'.ljust(25)} | {'Status'.ljust(25)} | {'Avaliacao'.ljust(25)}')
         for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.especialidade.ljust(25)} | {restaurante.ativo.ljust(25)} | {restaurante.media_avaliacao.ljust(25)} ')
    
    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alterar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self,cliente,nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacao(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return f'Não há avaliações'
        tot_notas= sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = tot_notas / len(self._avaliacao)
        return f'{media:.1f}'
    
    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print('=='*25)
        print(f'Cardapio do restaurante {self._nome}')
        print('=='*25)
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
        print('=='*25)