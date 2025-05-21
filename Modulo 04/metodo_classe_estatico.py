#Exemplo de codigo mostrando exemplo de metodos de classe e metodos estáticos
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nasc(cls, ano, mes, dia, nome):
        #print(cls)
        idade = 2025 - ano
        return Pessoa(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
p2 = Pessoa.criar_apartir_data_nasc(1996, 3, 12, "Antony")
print(p2.nome, p2.idade)

print(Pessoa.maior_idade(8))
print(Pessoa.maior_idade(38))