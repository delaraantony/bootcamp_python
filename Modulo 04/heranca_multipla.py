#O codigo abaixo exemplifica o uso de heraça multipla.
# # #Definindo a classe Animal

class Animal:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def fazer_som(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, nome, tipo, pelagem):
        super().__init__(nome, tipo)
        self.pelagem = pelagem

    def fazer_som(self):
        return "Som de mamífero"

class Ave(Animal):
    def __init__(self, nome, tipo, penas):
        super().__init__(nome, tipo)
        self.penas = penas

    def fazer_som(self):
        return "Som de ave"

class Cachorro(Mamifero):
    def __init__(self, nome, tipo, pelagem, raca):
        super().__init__(nome, tipo, pelagem)
        self.raca = raca

    def fazer_som(self):
        return "Au Au"

class Gato(Mamifero):
    def __init__(self, nome, tipo, pelagem, raca):
        super().__init__(nome, tipo, pelagem)
        self.raca = raca

    def fazer_som(self):
        return "Miau"

class Leao(Mamifero):
    def __init__(self, nome, tipo, pelagem, raca):
        super().__init__(nome, tipo, pelagem)
        self.raca = raca

    def fazer_som(self):
        return "Roar"

class Papagaio(Ave):
    def __init__(self, nome, tipo, penas, cor):
        super().__init__(nome, tipo, penas)
        self.cor = cor

    def fazer_som(self):
        return "Olá"

class Morcego(Mamifero, Ave):
    def __init__(self, nome, tipo, pelagem, penas):
        Mamifero.__init__(self, nome, tipo, pelagem)
        Ave.__init__(self, nome, tipo, penas)

    def fazer_som(self):
        return "Screech"

# Instanciando os objetos
cachorro = Cachorro("Rex", "Mamífero", "Curta", "Labrador")
gato = Gato("Mia", "Mamífero", "Longa", "Siamês")
leao = Leao("Simba", "Mamífero", "Densa", "Africano")
papagaio = Papagaio("Loro", "Ave", "Colorida", "Verde")
morcego = Morcego("Bruce", "Mamífero", "Curta", "Preta")

print (cachorro)
print (gato)
print (morcego)

leao.fazer_som()
papagaio.fazer_som()
#O código acima exemplifica a instancia de herança multipla.