from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_japones = Restaurante('Japa','Japonesa','Temaki')
bebida_suco= Bebida('Suco de Laranja',5.00,'Grande')
prato_temaki= Prato('Temaki',25.00,'Temaki de Salmão')
bebida_suco.aplicar_desconto()
prato_temaki.aplicar_desconto()
restaurante_japones.adicionar_no_cardapio(bebida_suco)
restaurante_japones.adicionar_no_cardapio(prato_temaki)

def main():
    restaurante_japones.exibir_cardapio

if __name__ == '__main__':
    main()