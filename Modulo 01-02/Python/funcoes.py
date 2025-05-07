#Exemplo de funções em Python

def exibir_mensagem():
    """
    Exibe uma mensagem na tela.
    
    Sem uso de parâmetros ou retorno.
    """
    print("Olá, mundo!")

def exibir_mensagem_com_parametro(mensagem):
    """
    Exibe uma mensagem na tela.
    
    Parâmetro:
    mensagem (str): A mensagem a ser exibida.
    
    Sem retorno.
    """
    print(mensagem)

def exibir_mensagem_com_padrao(mensagem="Olá, mundo!"):
    """
    Exibe uma mensagem na tela e retorna a mesma mensagem.
    
    Parâmetro:
    mensagem (str): A mensagem a ser exibida.
    
    Retorno:
    str: A mensagem exibida.
    """
    print(mensagem)

def exibir_mensagem_com_retorno(mensagem):
    """
    Exibe uma mensagem na tela e retorna a mesma mensagem.
    
    Parâmetro:
    mensagem (str): A mensagem a ser exibida.
    
    Retorno:
    str: A mensagem exibida.
    """
    print(mensagem)
    return mensagem

exibir_mensagem()
exibir_mensagem_com_parametro("Olá, mundo!")
exibir_mensagem_com_padrao() # Mensagem padrão
exibir_mensagem_com_retorno("Olá, mundo!") # Mensagem personalizada

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    """
    Retorna o antecessor e o sucessor de um número.
    
    Parâmetro:
    numero (int): O número para o qual se deseja encontrar o antecessor e o sucessor.
    
    Retorno:
    tuple: Uma tupla contendo o antecessor e o sucessor do número.
    """
    return numero - 1, numero + 1

def func_3():
   print("Função 3")

def salvar_Carro(marca, modelo, ano, placa):
    """
    Salva as informações de um carro em um dicionário.
    
    Parâmetros:
    marca (str): A marca do carro.
    modelo (str): O modelo do carro.
    ano (int): O ano do carro.
    placa (str): A placa do carro.
    
    Retorno:
    dict: Um dicionário contendo as informações do carro.
    """
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_Carro("Wolkswagen", "Fusca", 1980, "ABC-1234")  
salvar_Carro(marca="Wolkswagen", modelo="Fusca", ano=1980, placa="ABC-1234")
salvar_Carro(**{"marca": "Wolkswagen", "modelo": "Fusca", "ano": 1980, "placa": "ABC-1234"}) 

def exibir_poema(data_extenso, *args, **kwargs):
    """
    Exibe um poema com a data e os argumentos fornecidos.
    
    Parâmetros:
    data_extenso (str): A data em formato extenso.
    *args: Argumentos adicionais.
    **kwargs: Argumentos nomeados adicionais.
    
    Sem retorno.
    """
    texto = f"\n".join(args)
    meta_Dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n{texto}\n{meta_Dados}"
    print(mensagem)

exibir_poema(
    "Quarta-feira, 1 de outubro de 2023",
    "A vida é feita de escolhas.",
    "Hoje é um dia lindo!", 
    "A vida é bela.", 
    "Aproveite cada momento.", 
    autor="João", 
    data="2023-10-01"
)

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(f"Carro criado: {modelo}, {ano}, {placa}, {marca}, {motor}, {combustivel}")

criar_carro("Gol", 2020, "ABC-1234", "Volkswagen", "1.0", "Gasolina") # Valido
#criar_carro(modelo='Golf', ano=2020, placa='ABC-1234', marca='Volkswagen', motor='1.0', combustivel='Gasolina') # Invalido

def somar(a, b):
    """
    Soma dois números.
    
    Parâmetros:
    a (int ou float): O primeiro número.
    b (int ou float): O segundo número.
    
    Retorno:
    int ou float: A soma dos dois números.
    """
    return a + b

def exibir_Resultado(a, b, funcao):
    """
    Exibe o resultado de uma operação matemática.
    
    Parâmetros:
    a (int ou float): O primeiro número.
    b (int ou float): O segundo número.
    funcao (function): A função a ser aplicada aos números.
    
    Sem retorno.
    """
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} é igual a {resultado}")


exibir_Resultado(10, 20, somar) # Exibe o resultado da soma de 10 e 20
exibir_Resultado(10, 20, lambda a, b: a - b) # Exibe o resultado da subtração de 10 e 20

op = somar

print(op(1, 23)) # Exibe o resultado da soma de 1 e 23

salario = 2000

def salario_bonus(bonus):
    """
    Calcula o salário total com bônus.
    
    Parâmetro:
    bonus (int ou float): O valor do bônus.
    
    Retorno:
    int ou float: O salário total com bônus.
    """
    global salario
    salario += bonus
    return salario

resultado = salario_bonus(1000) # Adiciona um bônus de 1000 ao salário
print(resultado) # Exibe o salário total com bônus