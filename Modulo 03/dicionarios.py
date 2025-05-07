contatos = {
    "guilherme@gmail.com": {
        "nome": "Guilherme",
        "telefone": "12345-6789"},
    "giovana@gmail.com": {
        "nome": "Giovana",
        "telefone": "98765-4321"},
    "chappel@gmail.com": {
        "nome": "Chappel",
        "telefone": "55555-5555"},
    "melanie@gmail.com":{
        "nome": "Melanie",
        "telefone": "44444-4444",
        "extra": {
            "endereco": "Rua das Flores, 123",
            "data_nascimento": "01/01/1990",
            "notas": ["amiga de infância", "gosta de esportes"]
        }
    },
}
telefone = contatos["giovana@gmail.com"]["telefone"]
print(telefone) # 98765-4321

extra = contatos["melanie@gmail.com"]["extra"]
print(extra) # {'endereco': 'Rua das Flores, 123', 'data_nascimento': '01/01/1990', 'notas': ['amiga de infância', 'gosta de esportes']}

# Outro exemplo de dicionário

for chave in contatos:
    print(chave, contatos[chave])

# Outro exemplo de dicionário, agora com o metodo get()

contatos = {"guilhereme@gmail.com": {"nome": "Guilherme", "telefone": "12345-6789"}}

#contatos["chave"] # KeyError: 'chave'

resultado = contatos.get("chave")
print(resultado) # None

resultado = contatos.get("chave", {})
print(resultado) # {}

resultado = contatos.get(
    "guilherme@gmail.com", {}
)
print(resultado) # {'nome': 'Guilherme', 'telefone': '12345-6789'}

# Outro exemplo de dicionário, agora com o metodo keys()

contatos = {"antony@gmail.com": {"nome": "Antony", "telefone": "12345-6789"}}

resultado = contatos.keys()
print(resultado) # dict_keys(['antony@gmail.com'])

novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys()) # {'a': 100, 1: 'teste', 'b': 'python'}

# Outro exemplo de dicionário, agora com o metodo pop()
contatos = {"antony@gmail.com": {"nome": "Antony", "telefone": "12345-6789"}}

resultado = contatos.pop("antony@gmail.com")
print(resultado) # {'nome': 'Antony', 'telefone': '12345-6789'}

resultado = contatos.pop("antony@gmail.com", "não existe") # {}
print(resultado) # não existe

# Outro exemplo de dicionário, agora com o metodo setdefault()
contato = {"antony@gmail.com": {"nome": "Antony", "telefone": "12345-6789"}}

contato.setdefault("idade", 29) # Adiciona a chave idade com o valor 29 se não existir
print(contato) # {'nome': 'Antony', 'telefone': '12345-6789', 'idade': 29}

# Outro exemplo de dicionário, agora com o metodo 'in'

contatos = {
    "antony@gmail.com": {
        "nome": "Antony",
        "telefone": "12345-6789"},
    "natalia@gmail.com": {
        "nome": "Natalia",
        "telefone": "98765-4321"},
    "chappel@gmail.com": {
        "nome": "Chappel",
        "telefone": "55555-5555"},
    "olivia@gmail.com":{
        "nome": "Olivia",
        "telefone": "44444-4444",
    },
}

resultado = "antony@gmail.com" in contatos # True
print(resultado) # True

resultado = "guilherme@gmail.com" in contatos # False
print(resultado) # False

resultado = "idade" in contatos["antony@gmail.com"]
print(resultado) # False

resultado = "telefone" in contatos["antony@gmail.com"]
print(resultado) # True

carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
carro.get("motor") #