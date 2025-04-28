saldo = 200
saque = 200

# Variavel de comparacao
ehigual = saldo == saque
ehdiferente = saldo != saque
ehmaior = saldo > saque
ehmaiorigual = saldo >= saque
ehmenor = saldo < saque
ehmenorigual = saldo <= saque

# Verifica se o saldo é igual que o saque
if ehigual:
    print("Saque autorizado")

# Verifica se o saldo é diferente que o saque
if not ehdiferente:
    print("Saque não autorizado")

# Verifica se o saldo é maior que o saque
if not ehmaior:
    print("Saque autorizado")

# Verifica se o saldo é maior ou igual que o saque
if ehmaiorigual:
    print("Saque autorizado")

# Verifica se o saldo é menor que o saque
if not ehmenor:
    print("Saque não autorizado")

# Verifica se o saldo é menor ou igual que o saque
if ehmenorigual:
    print("Saque não autorizado")