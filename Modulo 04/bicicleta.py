#João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
#Para isso, será criado um programa onde será informado a: Cor, Modelo, Ano e Valor da bicicleta.
#Um bicicleta pode: buzinar, parar e correr.


#Definindo a classe Bicicleta
class Bicicleta:
    '''
    def __init__(self, c, m, a, v):
        self.cor = c
        self.modelo = m
        self.ano = a
        self.valor = v
    '''        

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("A bicicleta está buzinando!")

    def parar(self):
        print("A bicicleta parou!")

    def correr(self):
        print("A bicicleta está correndo!")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

'''
cor = input("Informe a cor da bicicleta: ")
modelo = input("Informe o modelo da bicicleta: ")
ano = int(input("Informe o ano da bicicleta: "))
valor = float(input("Informe o valor da bicicleta: "))
'''

b1 = Bicicleta("Vermelha", "Caloi", "2005", "350.00")
b2 = Bicicleta("Azul", "Monark", "2010", "450.00")
print(b1)
print(b2)
Bicicleta.buzinar(b1)
Bicicleta.parar(b1)
print("O pedestre passou na rua... ufa ele foi embora!")
Bicicleta.correr(b1)