usuarios = []
contas = []


# Uma função que verifica se o CPF já existe na lista de usuários
def encontrar_usuario(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

# Um função que faz o cadastro de um usuário, verificando se o CPF já existe na lista de usuários
def cadastrar_usuario():
    print("Cadastro de Usuário")
    cpf = input("CPF: ")
    if encontrar_usuario(cpf):
        print("Usuário já cadastrado.")
        return
    nome = input("Nome Completo:    ")
    nascimento = input("Data de Nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")
    """ 
    usuario = {
        'nome': nome,
        'cpf': cpf,
        'nascimento': nascimento,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    """
    usuarios.append({
        'nome': nome,
        'cpf': cpf,
        'nascimento': nascimento,
        'endereco': endereco
    })

    print("✅ Usuário cadastrado com sucesso!")

# Uma função que faz o cadastro de uma conta, verificando se o usuário existe na lista de usuários
def cadastrar_conta(agencia="0001"):
   cpf = input("Informe o CPF do usuário: ")
   usuario = encontrar_usuario(cpf)
   if not usuario:
       print("❌ Usuário não encontrado.")
       return
   
   senha = input("Informe a senha da conta: ")

   numero_conta = len(contas) + 1
   contas.append({
       "agencia": agencia,
       "numero": numero_conta,
       "usuario": usuario,
       "saldo": 0.0,
       "extrato": [],
       "limite_saque": 3,
       "saques_realizados": 0
   })

   print(f"✅ Conta cadastrada com sucesso! Número da conta: {numero_conta}")
# Uma função que autentica o usuário, verificando se a senha está correta
def autenticar(conta):
    senha = input("Informe a senha da conta: ")
    if senha == conta['senha']:
        return True
    else:
        print("❌ Senha incorreta.")
        return False
# Uma função que faz o depósito, verificando se o valor é válido e atualizando o saldo e o extrato
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("❌ Valor inválido para depósito.")
    return saldo, extrato
# Uma função que faz o saque, verificando se o valor é válido, se o saldo é suficiente e se o limite de saques foi atingido
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("❌ Limite de saques atingido.")
    elif valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print(f"❌ Valor excede o limite de R$ {limite:.2f} por saque maior que o permitido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("❌ Valor inválido para saque.")
    return saldo, extrato, numero_saques
# Uma função que exibe o extrato, mostrando o saldo e as transações realizadas
def exibir_extrato(saldo, *, extrato):
    print("\n=== 📄 Extrato da conta ===")
    if not extrato:
        print("Nenhum movimento realizado.")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=================\n")
#Uma função que lista todas as contas cadastradas, mostrando os dados do usuário e o número da conta
def listar_contas():
    if not contas:
        print("⚠️ Nenhuma conta cadastrada.")
        return

    print("\n=== 📋Listagem de Contas ===")
    for conta in contas:
        usuario = conta['usuario']
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | Nome: {usuario['nome']} | CPF: {usuario['cpf']}")
    print("=================\n")
# Uma função que seleciona uma conta, verificando se o número da conta existe e autenticando o usuário
def selecionar_conta():
    numero = int(input("Informe o número da conta: "))
    for conta in contas:
        if conta['numero'] == numero:
            if autenticar(conta):
                return conta
            else:
                return None
    print("❌ Conta não encontrada.")
    return None
# Uma função que valida o CPF, verificando se ele contém apenas dígitos e tem 11 caracteres
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11
# Menu principal do sistema bancário, que exibe as opções disponíveis e chama as funções correspondentes
def menu():
    sair = False
    while not sair:
        print("=== 🏦 Sistema Bancário ===")
        print("1. Cadastrar Usuário")
        print("2. Cadastrar Conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Extrato")
        print("6. Listar Contas")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            cadastrar_conta()
        elif opcao == "3":
            conta = selecionar_conta()
            if conta:
                if conta["transacoes"] >= conta["limite_transacoes"]:
                    print("⚠️ Limite de transações atingido.")
                    continue
                valor = float(input("Valor do depósito: R$ "))
                conta["saldo"], conta["extrato"] = depositar(conta["saldo"], valor, conta["extrato"])
                conta["transacoes"] += 1
        elif opcao == "4":
            conta = selecionar_conta()
            if conta:
                if conta["transacoes"] >= conta["limite_transacoes"]:
                    print("⚠️ Limite de transações atingido.")
                    continue
                valor = float(input("Valor do saque: R$ "))
                conta["saldo"], conta["extrato"], conta["saques_realizados"] = sacar(
                    saldo=conta["saldo"],
                    valor=valor,
                    extrato=conta["extrato"],
                    limite=500,
                    numero_saques=conta["saques_realizados"],
                    limite_saques=conta["limite_saque"]
                )
                conta["transacoes"] += 1
        elif opcao == "5":
            conta = selecionar_conta()
            if conta:
                exibir_extrato(conta["saldo"], extrato=conta["extrato"])
        elif opcao == "6":
            listar_contas()
        elif opcao == "7":
            print("✅ Saindo...")
            sair = True
            return
        else:
            print("❌ Opção inválida. Tente novamente.")
# Exibe o menu
menu()