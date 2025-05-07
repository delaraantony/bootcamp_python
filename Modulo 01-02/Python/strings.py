# Tipos de manipulação de strings em Python

# 1. Maiúsculas, Minúsculas e Título
texto = "python é incrível"
print(texto.upper())  # Converte para maiúsculas: "PYTHON É INCRÍVEL"
print(texto.lower())  # Converte para minúsculas: "python é incrível"
print(texto.title())  # Converte para formato de título: "Python É Incrível"

# 2. Eliminar espaços em branco
texto_com_espacos = "   Python   "
print(texto_com_espacos.strip())  # Remove espaços no início e no fim: "Python"
print(texto_com_espacos.lstrip())  # Remove espaços à esquerda: "Python   "
print(texto_com_espacos.rstrip())  # Remove espaços à direita: "   Python"

# 3. Junções
lista_palavras = ["Python", "é", "incrível"]
print(" ".join(lista_palavras))  # Junta palavras com espaço: "Python é incrível"
print("-".join(lista_palavras))  # Junta palavras com hífen: "Python-é-incrível"

# 4. Centralização
texto_centralizado = "Python"
print(texto_centralizado.center(20, "-"))  # Centraliza com preenchimento: "-------Python--------"
print(texto_centralizado.ljust(20, "-"))  # Alinha à esquerda: "Python---------------"
print(texto_centralizado.rjust(20, "-"))  # Alinha à direita: "---------------Python"

# 5. Interpolação de strings

# Old Style (%)
nome = "Python"
versao = 3.10
print("Linguagem: %s, Versão: %.2f" % (nome, versao))  # Linguagem: Python, Versão: 3.10

# Método format
print("Linguagem: {}, Versão: {:.2f}".format(nome, versao))  # Linguagem: Python, Versão: 3.10
print("Linguagem: {ling}, Versão: {ver:.2f}".format(ling=nome, ver=versao))  # Linguagem: Python, Versão: 3.10
print("Linguagem: {0}, Versão: {1}".format(nome, versao))  # Linguagem: Python, Versão: 3.10

# f-string
print(f"Linguagem: {nome}, Versão: {versao:.2f}")  # Linguagem: Python, Versão: 3.10

# Formatar strings com f-string
largura = 10
altura = 5
print(f"A área do retângulo com largura {largura} e altura {altura} é {largura * altura}.")
# A área do retângulo com largura 10 e altura 5 é 50.

# 6. Fatiamento de strings
frase = "Python é incrível"

# Acessar caracteres individuais
print(frase[0])  # Primeiro caractere: "P"
print(frase[-1])  # Último caractere: "l"

# Fatiar partes da string
print(frase[0:6])  # Do início até o índice 6 (não inclusivo): "Python"
print(frase[:6])  # Do início até o índice 6 (não inclusivo): "Python"
print(frase[7:])  # Do índice 7 até o final: "é incrível"
print(frase[::2])  # Pula de 2 em 2: "Pto írvl"
print(frase[::-1])  # Inverte a string: "levíicnir é nohtyP"

# 7. Strings de múltiplas linhas e strings triplas

# String de múltiplas linhas com aspas triplas
texto_multilinha = """Este é um exemplo
de uma string
com múltiplas linhas."""
print(texto_multilinha)

# String de múltiplas linhas com aspas simples triplas
texto_multilinha_simples = '''Outra forma de criar
uma string
com múltiplas linhas.'''
print(texto_multilinha_simples)

# Strings triplas também podem ser usadas para comentários de múltiplas linhas
"""
Este é um comentário de múltiplas linhas.
Ele não será executado como código.
"""