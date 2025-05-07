# Estruturas de repetição em Python

# 1. Laço "for"
# Utilizado para iterar sobre uma sequência (como listas, strings, ranges, etc.)
'''
for i in range(5):  # Itera de 0 a 4
    print(f"For loop: {i}")
'''
# Exemplo de laço "for" com lista
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(f"Número: {numero}")
# Exemplo de laço "for" com string
texto = "Python"
for letra in texto:
    print(f"Letra: {letra}")
# Exemplo de laço "for" com condicional e string
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(f"Vogal encontrada: {letra}", end=" \n")
    else:
        print(f"Consoante encontrada: {letra}", end=" \n")
print()  # Para pular linha após o loop
# 2. Laço "while"
# Executa enquanto a condição for verdadeira
contador = 0
while contador < 5:
    print(f"While loop: {contador}")
    contador += 1

# 3. Combinando "for" com "else"
# O bloco "else" é executado quando o laço termina normalmente (sem interrupção por "break")
for i in range(0,51,5):
    print(f"For with else: {i}")
else:
    print("For loop terminou normalmente.")

# 4. Combinando "while" com "else"
# O bloco "else" é executado quando o laço termina normalmente (sem interrupção por "break")
'''
contador = 0
while contador < 3:
    print(f"While with else: {contador}")
    contador += 1
else:
    print("While loop terminou normalmente.")
'''
opcao = -1
while opcao !=0:
    opcao = int(input("Escolha uma opção (1 - Sacar, 2 - Extrato, 0 para sair): "))
    if opcao == 1:
        print("Saque realizado com sucesso!")
    elif opcao == 2:
        print("Extrato exibido com sucesso!")
    elif opcao == 0:
        print("Saindo...")
    else:
        print("Opção inválida! Tente novamente.")
# 5. Uso do "break" para interromper um laço
for i in range(10):
    if i == 5:
        print("Break no loop for")
        break

# 6. Uso do "continue" para pular uma iteração
for i in range(5):
    if i == 2:
        continue  # Pula o restante do código nesta iteração
    print(f"Continue no loop for: {i}")

# 7. Uso do "pass" como placeholder
for i in range(5):
    if i == 3:
        pass  # Não faz nada, apenas um placeholder
    print(f"Pass no loop for: {i}")