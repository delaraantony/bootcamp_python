#Exemplificando uso de construtores e destrutores utilizando a classe Cachorro.
# #Definindo a classe Cachorro
class Cachorro:
    def __init__(self, nome, raca, idade, acordado=True):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.acordado = acordado
        print(f"Cachorro {self.nome} criado!")

    def __del__(self):
        print(f"Cachorro {self.nome} destruído!")
    
    def latir(self):
        print(f"{self.nome} está latindo!")

    def dormir(self):
        self.acordado = False
        print(f"{self.nome} está dormindo!")

c = Cachorro("Rex", "Labrador", 5)
c.latir()