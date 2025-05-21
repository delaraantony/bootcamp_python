#Exemplo de codigo com uso de propriedades
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def get_nome(self):
        return self._nome
    
    @property
    def idade(self):
        from datetime import date
        ano_atual = date.today().year
        return ano_atual - self._ano_nascimento

p = Pessoa('Antony', 1996)
print(f"Nome: {p.get_nome} \tIdade: {p.idade}")
# A propriedade idade é calculada com base no ano atual e no ano de nascimento