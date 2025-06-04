''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

#TODO: Implemente a classe SistemaBancario:
class SistemaBancario:
    def __init__(self):
      # TODO: Inicialize a lista de contas:
      self.conta = []
      
    def criar_conta(self, titular, saldo):
      # TODO: Crie uma nova conta e adicione à lista de contas:
      conta = ContaBancaria(titular, saldo)
      self.contas.append(conta)

    def listar_contas(self):
      # TODO: Liste todas as contas no formato "Titular: R$ Saldo":
      for conta in self.contas:
        print(f"{conta.titular}: R$ {conta.saldo:.2f}")

#TODO: Crie uma instância de SistemaBancario:
sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    try:
        titular, saldo = entrada.split(", ")
        sistema.criar_conta(titular, float(saldo))
    except ValueError:
        print("Entrada inválida. Use o formato 'Titular, SaldoInicial'.")

sistema.listar_contas()