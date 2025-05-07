# Exemplo de declaração de conjuntos em Python

# Criando conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = set([3, 4, 5, 6, 7])

# Exibindo os conjuntos
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

linguagens = {'Python', 'Java', 'C++', 'JavaScript', 'C#'}
print("Linguagens:", linguagens)


# Removendo elementos a um conjunto
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("Números:", numeros) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(numeros.pop()) # Remove e retorna um elemento aleatório do conjunto
print(numeros.pop()) # Remove e retorna um elemento aleatório do conjunto
print(numeros) # {3, 4, 5, 6, 7, 8, 9, 10}