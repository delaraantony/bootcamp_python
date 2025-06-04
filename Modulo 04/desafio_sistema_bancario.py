class ContaBancaria:
    # TODO: Inicialize a conta bancária com o nome do titular, saldo 0 e  liste para armazenar as operações realizadas:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.operacoes = []

    # TODO: Implemente o método para realizar um depósito, adicione o valor ao saldo e registre a operação:
    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f'+{valor}')

    # TODO: Implemente o método para realizar um saque:
    def sacar(self, valor):
        # TODO: Verifique se há saldo suficiente para o saque
        if valor == 0:
            self.operacoes.append('0')
            return
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(f'-{valor}')
        else:
            self.operacoes.append('Saque não permitido')

            # TODO: Registre a operação e retorne a  mensagem de saque negado
            

    # TODO: Crie o método para exibir o extrato da conta e junte as operações no formato correto:
    def extrato(self):
        operacoes_str = ', '.join(self.operacoes)
        return f'Operações: {operacoes_str}; Saldo: {self.saldo}'

nome_titular = input().strip()  
conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)  
    else:
        conta.sacar(valor)  

print(conta.extrato())