# [].Copy

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()  # Copia a lista
print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)

# [].Extend

linguagens = ['Python', 'Java', 'C++']

print(linguagens) # ['Python', 'Java', 'C++']

linguagens.extend(['JavaScript', 'C#']) # Adiciona os elementos da lista ao final da lista

print(linguagens) # ['Python', 'Java', 'C++', 'JavaScript', 'C#']

# [].Index

linguagens = ['Python', 'Java', 'C++', 'JavaScript', 'C#']

print(linguagens.index('Java')) # 1
print(linguagens.index('Python')) # 0

# [].Remove

linguagens = ['Python', 'Java', 'C++', 'JavaScript', 'C#']
print(linguagens) # ['Python', 'Java', 'C++', 'JavaScript', 'C#']

linguagens.remove('Java') # Remove o primeiro elemento que for igual a 'Java'
print(linguagens) # ['Python', 'C++', 'JavaScript', 'C#']

# Sorted
linguagens = ['Python', 'Java', 'C++', 'JavaScript', 'C#']

print(sorted(linguagens, key=lambda x: len(x))) # ['C#', 'C++', 'Java', 'Python', 'JavaScript'] 
print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # ['JavaScript', 'Python', 'Java', 'C++', 'C#']   

print(sorted(linguagens)) # ['C#', 'C++', 'Java', 'JavaScript', 'Python']
print(sorted(linguagens, reverse=True)) # ['Python', 'JavaScript', 'Java', 'C++', 'C#']
