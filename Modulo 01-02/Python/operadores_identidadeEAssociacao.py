# Operadores de Identidade: 'is' e 'is not'
a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]

# 'is' verifica se duas variáveis referem-se ao mesmo objeto na memória
print(a is b)  # True, pois ambos referem-se ao mesmo objeto imutável
print(c is d)  # False, pois listas são objetos mutáveis e têm endereços diferentes

# 'is not' verifica se duas variáveis NÃO referem-se ao mesmo objeto na memória
print(a is not b)  # False
print(c is not d)  # True

# Operadores de Associação: 'in' e 'not in'
lista = [1, 2, 3, 4, 5]
texto = "Python"

# 'in' verifica se um elemento está presente em uma sequência
print(3 in lista)  # True
print("Py" in texto)  # True

# 'not in' verifica se um elemento NÃO está presente em uma sequência
print(6 not in lista)  # True
print("Java" not in texto)  # True

#Exemplo pratico
x = (22 - 10) * 3
print(x)
print(5 is x) # False, pois x é 36 e não 5 -> Compreensivel, tenha um bom dia :|