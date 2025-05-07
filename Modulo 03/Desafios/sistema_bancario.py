# Parte 1 - Estabelecer um limite de 10 transações diárias para uma conta.
# Parte 2 - Se o usuario tentar fazer uma transição após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas.
# Parte 3 - Mostrar no extrato, a data e hora de todas as transações.
from datetime import datetime

# Limite de transações diárias
limte_diario = 10
transacoes_realizadas = 0
extrato = [] # Lista para armazenar as transações

def permissao_transacao():
    return transacoes_realizadas < limte_diario

def realizar_transacao(valor):
    global transacoes_realizadas
    if permissao_transacao():
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f"{agora} - Transação de R$ {valor:.2f}")
        print(f"Transação realizada com sucesso no valor de R$ {valor:.2f}")
        transacoes_realizadas += 1
    else:
        print("Limite de transações diárias atingido. Tente novamente mais tarde.")

def mostrar_extrato():
    print("\nExtrato de Transações:")
    if extrato:
        for transacao in extrato:
            print(transacao)
    else:
        print("Nenhuma transação realizada.")

def menu():
    while True:
        print("\n-------------------")
        print("Sistema Bancário")
        print("1. Realizar Transação")
        print("2. Verificar transações restantes")
        print("3. Sair")
        print("-------------------\n")
        op = input("Escolha uma opção: ")
        if op == '1':
            valor = float(input("Digite o valor da transação: R$ "))
            realizar_transacao(valor)
        elif op == '2':
            restantes = limte_diario - transacoes_realizadas
            print(f"Transações restantes: {restantes}")
        elif op == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
