menu = """

[d] -> Depositar
[s] -> Sacar
[e] -> Extrato
[q] -> Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = input(menu).lower()
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Valor inválido para saque.")
        elif excedeu_limite:
            print("Valor acima do limite de saque.")
        elif excedeu_limite:
            print("Número máximo de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor informado é inválido para saque.")
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")