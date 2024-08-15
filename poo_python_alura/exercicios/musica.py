class Musica:
    playlist= []

    def __init__(self,nome,artista,duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.playlist.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.artista}'
    
    def show_playlist():
        for musica in Musica.playlist:
            print(f'{musica.nome}  | {musica.artista}')
    
    

carti = Musica('Foreign','Carti','153')
derek = Musica('Bonde do ó','Derek','144')

Musica.show_playlist()