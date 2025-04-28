# Exemplo de indentação em blocos de código no Python

# Bloco de função
def sacar(valor):
    saldo=500
    if saldo >= valor:  # Bloco de condição
        print(f"Olá, visitante! O valor de {valor} foi sacado")  # Bloco de instrução
    else:
        print(f"Olá, visitante! não foi possivel sacar esse valor de {valor}")  # Bloco de instrução
sacar(1000)

# Bloco de loop
for i in range(3):
    print(f"Contagem: {i}")  # Bloco de instrução dentro do loop

# Bloco de classe
class Pessoa:
    def __init__(self, nome, idade):  # Bloco de método
        self.nome = nome
        self.idade = idade

    def apresentar(self):  # Bloco de método
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

# Chamando as funções e métodos
#saudacao("Antony")
pessoa = Pessoa("Antony", 29)
pessoa.apresentar()