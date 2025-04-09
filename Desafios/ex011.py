# Desafio 11
altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))
# area = altura * largura
# tinta = area / 2
# print("A área da parede é de {} m² e você precisará de {} litros de tinta para pintá-la.".format(area, tinta))
# O mesmo que:
area = altura * largura
tinta = area / 2
print("A parede possui uma dimensão de {}x{}. ".format(altura, largura), end="")
print("A área da parede é de {:.2f} m² e você precisará de {:.2f} litros de tinta para pintá-la.".format(area, tinta))