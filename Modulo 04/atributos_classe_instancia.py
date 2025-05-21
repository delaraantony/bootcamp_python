#O codigo abaixo exemplifica o uso de variaveis de classe com atributos e instância
class Estudante:
    # Atributo de classe
    escola = "Escola XYZ"
    
    def __init__(self, nome, numero):
        # Atributo de instância
        self.nome = nome
        self.numero = numero

    def __str__(self) -> str:
        return f"{self.nome} - {self.numero} - {self.escola}"    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

# Criando instâncias da classe Estudante
gui = Estudante("Guilherme", 123)
gi = Estudante("Giovanna", 456)
mostrar_valores(gui, gi)

Estudante.escola = "Escola ABC"  # Alterando o atributo de classe 
aluno3 = Estudante("Ana", 789)  # Criando nova instância
mostrar_valores(gui, gi, aluno3)  # Mostrando os valores