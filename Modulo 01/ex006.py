# Desafio 6
num = int(input("Digite um número: "))
print("Analisando o número {}".format(num))
#dob = num * 2
#tri = num * 3
#raiz = num ** (1/2)
#cub = num ** (1/3)
print("O dobro do valor de {} é {}".format(num, num * 2))
print("O triplo do valor de {} é {}".format(num, num * 3))
print("A raiz quadrada do valor de {} é {:.2f}".format(num, num ** (1/2)))
print("A raiz cúbica do valor de {} é {:.2f}".format(num, num ** (1/3)))
# O mesmo que:
# print("O dobro do valor de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}".format(num, num * 2, num * 3, num ** (1/2)))