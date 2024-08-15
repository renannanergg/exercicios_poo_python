from livro import Livro

# Instanciando dois objetos da classe Livro
livro_A = Livro('A', 'Autor A', 2010)
livro_B = Livro('B', 'Autor B', 2015)

# Exibindo a mensagem formatada utilizando o método __str__
print(livro_A)
print(livro_B)

def main():
    Livro.listar_livros()

if __name__ == '__main__':
    main()  