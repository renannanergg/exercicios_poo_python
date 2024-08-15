class Carros:
    def __init__(self,modelo,cor,ano):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano
    
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
    def print_carros(self):
        print(f'{self.modelo} | {self.ano} | {self.cor}')
    

jeep_compass=Carros('SUV','Branco Perolado','2024')
Carros.print_carros(jeep_compass)
