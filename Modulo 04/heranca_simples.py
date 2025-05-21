#O codigo abaixo exemplifica o uso de heraça simples.
# #Definindo a classe Veiculo

class Veiculo:
    def __init__(self, cor, modelo, ano, valor, placa):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.placa = placa

    def ligar_motor(self):
        print("O motor está ligado!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, modelo, ano, valor, placa, carregado):
        super().__init__(cor, modelo, ano, valor, placa) 
        self.carregado = carregado

    def esta_carregado(self):
        print(f"O caminhão está carregado? {"Sim" if self.carregado else "Não"}")


moto = Motocicleta("Preta", "Honda", 2020, 15000, "ABC-1234")   
carro = Carro("Vermelho", "Fusca", 1970, 20000, "XYZ-5678")
caminhao = Caminhao("Branco", "Volvo", 2015, 80000, "LMN-9101", False)
print(moto, "\n", carro, "\n", caminhao)
#O código acima exemplifica a instancia de herança simples.