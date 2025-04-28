nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

#print("Muito prazer em te conhecer", nome, ", sua idade é", idade, "anos.")
print(f"Muito prazer em te conhecer {nome}, sua idade é {idade} anos.")
print("Teste", end=" ")
print(nome, idade, end="...")
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")