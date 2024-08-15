from livro import Livro

#Utilizando metodo de emprestar um livro
livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca._disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca._disponivel}")

#Utilizando metodo de verificar disponibilidade
Livro.verificar_disponibilidade()


