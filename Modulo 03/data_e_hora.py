#Exenplos com datetime, date e time

from datetime import date, time, datetime

data = date(2023, 10, 1) # Cria um objeto date com o ano, mês e dia especificados
# data = date.today() # Cria um objeto date com a data atual
#print(data) # 2023-10-01

data_hora = datetime(2023, 10, 1, 12, 30, 45) # Cria um objeto datetime com o ano, mês, dia, hora, minuto e segundo especificados
# data_hora = datetime.now() # Cria um objeto datetime com a data e hora atual
#print(data_hora) # 2023-10-01 12:30:45
#print(data_hora.today()) # 2023-10-01 12:30:45

hora = time(12, 30, 45) # Cria um objeto time com a hora, minuto e segundo especificados
#print(hora) # 12:30:45

#Exemplos com timedelta

from datetime import timedelta

tipo_carro = "G" # P = pequeno, M = medio, G = grande
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now() # Cria um objeto datetime com a data e hora atual

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno) # Adiciona 30 minutos à data atual
    print(f"Chegada do Carro: {data_atual}\nEstará pronto: {data_estimada}") # 2023-10-01 13:00:45
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio) # Adiciona 45 minutos à data atual
    print(f"Chegada do Carro: {data_atual}\nEstará pronto: {data_estimada}") # 2023-10-01 13:00:45
elif tipo_carro == "G":
    data_estimada = data_atual + timedelta(minutes=tempo_grande) # Adiciona 60 minutos à data atual 
    print(f"Chegada do Carro: {data_atual}\nEstará pronto: {data_estimada}") # 2023-10-01 13:00:45
else:
    print("Tipo de carro inválido")
    exit()

print(date.today() - timedelta(days=1)) # 2023-10-01 13:00:45

resultado = datetime(2025,4,27, 12,30,45) - timedelta(days=1) # Subtrai 1 dia da data especificada
print(resultado.time)

# Exemplos com strftime e strptime

data_hora_atual = datetime.now() # Cria um objeto datetime com a data e hora atual
data_hora_str = "2024-10-01 12:30:45" # String com a data e hora no formato YYYY-MM-DD HH:MM:SS
mascara_ptbr = "%d/%m/%Y %a" # Máscara para o formato brasileiro
mascara_en = "%Y-%m-%d %H:%M:%S" # Máscara para o formato americano

print(data_hora_atual.strftime(mascara_ptbr)) # Converte o objeto datetime para string no formato brasileiro

print(datetime.strptime(data_hora_str, mascara_en)) # Converte a string para objeto datetime no formato americano

# Exemplos com pytz
import pytz

data = datetime.now(pytz.timezone('Europe/Rome')) # Cria um objeto datetime com a data e hora atual no fuso horário de Campo Grande

print(data)

# Exemplos com timezone
from datetime import timezone

data_rome = datetime.now(timezone(timedelta(hours=2))) # Cria um objeto datetime com a data e hora atual no fuso horário de Roma
data_cg = datetime.now(timezone(timedelta(hours=-4))) # Cria um objeto datetime com a data e hora atual no fuso horário de Campo Grande
data_utc = datetime.now(timezone.utc) # Cria um objeto datetime com a data e hora atual no fuso horário UTC

print(data_rome) # 2023-10-01 12:30:45+01:00
print(data_cg) # 2023-10-01 12:30:45-04:00
print(data_utc) # 2023-10-01 12:30:45+00:00