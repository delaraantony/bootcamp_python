#Exemplo de codigo Python com uso de polimorfismo
class Passaro:
    def voar(self):
        print("O pássaro está voando.")
        pass

class Pardal(Passaro):
    def voar(self):
        print("O pardal está voando baixo.")
        pass

class Avestruz(Passaro):
    def voar(self):
        print("O avestruz não pode voar.")
        pass

class Papagaio(Passaro):
    def voar(self):
        print("O papagaio está voando alto.")
        pass

class Aviao(Passaro):
    def voar(self):
        print("O avião está voando a alta velocidade.")
        print("Compreensivel, tenha um bom dia")
        pass

def plano_de_voo(passaro):
    passaro.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())	
plano_de_voo(Papagaio())
plano_de_voo(Aviao())
# A função plano_de_voo aceita qualquer objeto que tenha o método voar, demonstrando o conceito de polimorfismo.