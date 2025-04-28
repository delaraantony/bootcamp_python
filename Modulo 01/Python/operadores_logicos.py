# Exemplos de operadores lógicos em Python
a = True
b = False

# Operador AND (e)
resultado_and = a and b  # Retorna True se ambos forem True
print(f"Resultado de AND: {resultado_and}")

# Operador OR (ou)
resultado_or = a or b  # Retorna True se pelo menos um for True
print(f"Resultado de OR: {resultado_or}")

# Operador NOT (não)
resultado_not = not a  # Inverte o valor lógico
print(f"Resultado de NOT: {resultado_not}")

# Exemplo pratico
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(f"Resultado da expressão 1: {exp1}")
print(f"Resultado da expressão 2: {exp2}")

# Verifica se as contas tem saldo suficiente para o saque
contaNormal_com_saldo = saldo >= saque and saque <= limite
contaEspecial_com_saldo = conta_especial and saldo >= saque
if not contaNormal_com_saldo:
    print("Você não possui saldo suficiente para o saque.")
if contaEspecial_com_saldo:
    print("Você possui saldo suficiente para o saque.")
# Exibe o resultado das contas

#print(contaNormal_com_saldo)
#print(contaEspecial_com_saldo)
