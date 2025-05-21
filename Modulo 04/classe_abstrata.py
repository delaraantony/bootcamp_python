from abc import ABC, abstractmethod
# Exemplo de código Python com uso de classe abstrata
class ControleRemoto(ABC):
    @abstractmethod 
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("A TV está ligada.")
    def desligar(self):
        print("A TV está desligada.")

class ControleSom(ControleRemoto):
    def ligar(self):
        print("O som está ligado.")
    def desligar(self):
        print("O som está desligado.")  

controleTV = ControleTV()
controleTV.ligar()
controleTV.desligar()
print("\n")
csom = ControleSom()
csom.ligar()
csom.desligar()

# A classe ControleRemoto é uma classe abstrata que define os métodos ligar e desligar, mas não os implementa.