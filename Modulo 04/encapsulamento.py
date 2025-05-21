#Um exemplo de codigo utilizando encapsulamento.
class ContaBancaria:
    def __init__(self, n_agencia,saldo=0):
        self.saldo = saldo
        self.n_agencia = n_agencia
    
    def depositar (self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")
    
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")
    
    def mostrar_saldo(self):
        return self.saldo
    

conta = ContaBancaria("0001", 100);
conta.depositar(50)
print (conta.n_agencia)
print (conta.mostrar_saldo())