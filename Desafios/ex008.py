# Desafio 8
m = float(input("Digite a distancia em metros: "))
#print("A medida de {}m corresponde a:".format(m))
#print("Em centímetros: {}cm".format(m * 100))
#print("Em milímetros: {}mm".format(m * 1000))
#print("Em decímetros: {}dm".format(m * 10))
#print("Em hectômetros: {}hm".format(m / 100))
#print("Em quilômetros: {}km".format(m / 1000))
#O mesmo que:
print("A medida de {}m corresponde a \n{}cm, \n{}mm, \n{}dm, \n{}hm e \n{}km".format(m, m * 100, m * 1000, m * 10, m / 100, m / 1000))
