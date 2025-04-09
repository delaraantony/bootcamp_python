# Desafio 5 
num = int(input("Digite um número: "))
print("Analisando o número {}".format(num))
#print("Seu antecessor é {}".format(num - 1))
#print("Seu sucessor é {}".format(num + 1))
print("O seu antecessor é {}".format(num - 1), end=",")
print(" e o seu sucessor é {}".format(num + 1))
# O mesmo que:
# print("O seu antecessor é {} e o seu sucessor é {}".format(num - 1, num + 1))