# Exemplo de estrutura condicional simples
'''
x = 10
if x > 5:
    print("x é maior que 5")
'''
saldo = 2000.0
saque = float(input("Digite o valor do saque: "))
if saldo >= saque:
    saldo -= saque
    print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
if saldo <= saque:
    print("Saldo insuficiente para realizar o saque.")
# Exemplo de estrutura condicional com else
'''
y = 3
if y % 2 == 0:
    print("y é par")
else:
    print("y é ímpar")
'''
saldo = 2000.0
saque = float(input("Digite o valor do saque: "))
if saldo >= saque:
    saldo -= saque
    print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
else:
    print("Saldo insuficiente para realizar o saque.")

# Exemplo de estrutura condicional com elif
'''
z = 15
if z < 10:
    print("z é menor que 10")
elif z == 10:
    print("z é igual a 10")
else:
    print("z é maior que 10")
'''
opcao = int(input("Escolha uma opção ([1]-> Sacar. \n[2]-> Extrato): "))
if opcao == 1:
    saque = float(input("Digite o valor do saque: "))
    if saldo >= saque:
        saldo -= saque
        print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente para realizar o saque.")
elif opcao == 2:
    print(f"Seu saldo atual é: R$ {saldo:.2f}")
else:
    print("Opção inválida. Tente novamente.")
# Exemplo de estrutura condicional aninhada
'''
a = 7
b = 20
if a > 5:
    if b > 15:
        print("a é maior que 5 e b é maior que 15")
'''
conta_normal = False
cheque_especial = 500
conta_universitaria = True

if conta_normal:
    if saldo >= saque:
        print("Saque da conta normal realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saldo realizado com cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque da conta universitario realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")
else:
    print("Conta inválida. Verifique os dados e tente novamente.")
# Exemplo de operador ternário
'''
idade = 18
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)
'''
saldo = 2000.0
saque = 1500.0

status = "Sucesso" if saldo >= saque else "Saldo insuficiente"
print(f"{status} ao realizar o saque!")