from class_endereco import Endereco
from class_cliente import Cliente
from class_funcionario import Funcionario
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_produto import Produto
from class_mesa import Mesa
from class_nota_fiscal import NotaFiscal


clientes = []
funcionarios = []
mesas = []
enderecos = []
produtos = []
pedidos = []

def menu_principal():
    print('''
        MENU Principal:
        [1] - Cliente
        [2] - Funcionário
        [3] - Produto
        [4] - Pedido
        [5] - Mesa
        [s] - Sair
    ''')
    return input('Escolha uma opção: ')

def menu_cliente():
    while True:
        print('''
        MENU de Clientes:
        [1] - Cadastrar Cliente
        [2] - Visualizar Clientes
        [s] - Sair
        ''')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == 's':
            print("Saindo do menu de cliente.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_funcionario():
    while True:
        print('''
        MENU de Funcionários:
        [1] - Cadastrar Funcionário
        [2] - Visualizar Funcionários
        [s] - Sair
        ''')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            listar_funcionarios()
        elif opcao == 's':
            print("Saindo do menu de funcionário.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_pedido():
    while True:
        print('''
        MENU de Pedidos:
        [1] - Cadastrar Pedido
        [2] - Concluir Pedido
        [3] - Visualizar Pedidos
        [4] - Adicionar Produto ao Pedido
        [5] - Associar Cliente e Funcionário ao Pedido
        [s] - Sair
        ''')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_pedido()
        elif opcao == '2':
            concluir_e_remover_pedido()
        elif opcao == '3':
            visualizar_pedidos()
        elif opcao == '4':
            adicionar_produto_ao_pedido()
        elif opcao == '5':
            adicionar_cliente_e_funcionario_ao_pedido()  # Chama a nova função criada
        elif opcao == 's':
            print("Saindo do menu de pedidos.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_produtos():
    while True:
        print('''
        MENU de Produtos:
        [1] - Cadastrar Produto
        [2] - Remover Produto
        [3] - Pesquisar Produto
        [4] - Listar Produtos
        [s] - Sair
        ''')
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            remover_produto()
        elif opcao == '3':
            pesquisar_produto()
        elif opcao == '4':
            listar_produtos()
        elif opcao == 's':
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    while True:
        opcao = menu_principal()

        if opcao == '1':
            menu_cliente()
        elif opcao == '2':
            menu_funcionario()
        elif opcao == '3':
            menu_produtos()
        elif opcao == '4':
            menu_pedido()
        elif opcao == '5':
            cadastrar_mesa()
        elif opcao == 's':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")



##### funções para uso

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone do cliente: ")
    cpf = input("CPF do cliente (somente numero): ")
    email = input("Email do cliente: ")
    senha = input("Senha do cliente: ")
    data_nascimento = input("Data de nascimento do cliente (somente numero): ")

    endereco_entrega = selecionar_ou_cadastrar_endereco()

    novo_cliente = Cliente(nome, cpf, email, telefone, endereco_entrega, data_nascimento, senha)

    clientes.append(novo_cliente)

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("Lista de clientes:")
        for cliente in clientes:
            cliente.listar()

def cadastrar_funcionario():
    id = input("Digite o ID do funcionário: ")
    nome = input("Digite o nome do funcionário: ")
    telefone = input("Telefone do funcionário: ")
    cpf = input("Digite o CPF do funcionário (somente numero): ")
    email = input("Digite o email do funcionário: ")
    senha = input("Digite a senha do funcionário: ")
    data_nascimento = input("Digite a data de nascimento do funcionário (somente numero): ")

    endereco_entrega = selecionar_ou_cadastrar_endereco()

    novo_funcionario = Funcionario(nome, cpf, email, telefone, endereco_entrega, data_nascimento, senha, id)
    funcionarios.append(novo_funcionario)
    print(f"Funcionário {novo_funcionario._id} cadastrado com sucesso!")

def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionario cadastrado.")
    else:
        print("Lista de funcionários:")
        for funcionario in funcionarios:
            funcionario.listar()

def cadastrar_produto():
    codigo_produto = input("Digite o código do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    validade = input("Digite a validade do produto: ")

    novo_produto = Produto(codigo_produto, descricao, preco, validade)
    produtos.append(novo_produto)
    print(f"Produto {novo_produto._codigo_produto} cadastrado com sucesso!")

def remover_produto():
    codigo_produto = input("Digite o código do produto que deseja remover: ")

    for produto in produtos:
        if produto._codigo_produto == codigo_produto:
            produtos.remove(produto)
            print(f"Produto {codigo_produto} removido com sucesso!")
            break
    else:
        print(f"Produto {codigo_produto} não encontrado.")

def pesquisar_produto():
    codigo_produto = input("Digite o código do produto que deseja pesquisar: ")

    for produto in produtos:
        if produto._codigo_produto == codigo_produto:
            print(f"Produto encontrado: {produto._descricao}, Preço: {produto._preco}, Validade: {produto._validade}")
            break
    else:
        print(f"Produto {codigo_produto} não encontrado.")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de Produtos:")
        for produto in produtos:
            print(f"Código: {produto._codigo_produto}, Descrição: {produto._descricao}, Preço: {produto._preco}, Validade: {produto._validade}")

def cadastrar_pedido():
    codigo_pedido = input("Digite o código do pedido: ")

    if any(pedido._codigo_pedido == codigo_pedido for pedido in pedidos):
        print(f"Já existe um pedido com o código {codigo_pedido}.")
        return

    mesa_numero = input("Digite o número da mesa (deixe em branco para não associar a uma mesa): ")
    mesa = encontrar_mesa_por_numero(mesa_numero)

    novo_pedido = Pedido(codigo_pedido)

    if mesa:
        mesa._pedidos.append(novo_pedido)
        pedidos.append(novo_pedido)
        print(f"Pedido {novo_pedido._codigo_pedido} associado à mesa {mesa._numero_da_mesa}.")
    else:
        pedidos.append(novo_pedido)
        print(f"Pedido {novo_pedido._codigo_pedido} cadastrado com sucesso!")

def encontrar_mesa_por_numero(numero_mesa):
    for mesa in mesas:
        if mesa._numero_da_mesa == numero_mesa:
            return mesa
    return None

def encontrar_produto_por_codigo(codigo_produto):
    for produto in produtos:
        if produto._codigo_produto == codigo_produto:
            return produto
    return None

def escolher_forma_de_pagamento():
    while True:
        print("Escolha a forma de pagamento:")
        print("1. Pix")
        print("2. Cartão de Crédito")
        print("3. Cartão de Débito")
        print("4. Dinheiro")
        print("0. Voltar")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            return "pix"
        elif opcao == '2':
            return "cartao de credito"
        elif opcao == '3':
            return "debito"
        elif opcao == '4':
            return "dinheiro"
        elif opcao == '0':
            return None
        else:
            print("Opção inválida. Tente novamente.")


def adicionar_cliente_e_funcionario_ao_pedido():
    # Verificar se existem clientes e funcionários cadastrados
    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return
    if not funcionarios:
        print("Nenhum funcionário cadastrado. Cadastre um funcionário primeiro.")
        return

    # Listar clientes disponíveis
    print("Clientes disponíveis:")
    for i, cliente in enumerate(clientes):
        print(f"{i + 1}: {cliente._nome}")  # Corrigindo para usar o atributo correto

    cliente_numero = input("Digite o número do cliente desejado: ")
    try:
        cliente_numero = int(cliente_numero)
        if 1 <= cliente_numero <= len(clientes):
            cliente_selecionado = clientes[cliente_numero - 1]
        else:
            print("Número de cliente inválido.")
            return
    except ValueError:
        print("Número de cliente inválido.")
        return

    # Listar funcionários disponíveis
    print("Funcionários disponíveis:")
    for i, funcionario in enumerate(funcionarios):
        print(f"{i + 1}: {funcionario._nome}")  # Corrigindo para usar o atributo correto

    funcionario_numero = input("Digite o número do funcionário desejado: ")
    try:
        funcionario_numero = int(funcionario_numero)
        if 1 <= funcionario_numero <= len(funcionarios):
            funcionario_selecionado = funcionarios[funcionario_numero - 1]
        else:
            print("Número de funcionário inválido.")
            return
    except ValueError:
        print("Número de funcionário inválido.")
        return

    # Listar pedidos disponíveis
    print("Pedidos disponíveis:")
    for i, pedido in enumerate(pedidos):
        print(f"{i + 1}: Código do Pedido - {pedido._codigo_pedido}")

    pedido_numero = input("Digite o número do pedido ao qual deseja adicionar cliente e funcionário: ")
    try:
        pedido_numero = int(pedido_numero)
        if 1 <= pedido_numero <= len(pedidos):
            pedido_selecionado = pedidos[pedido_numero - 1]
        else:
            print("Número de pedido inválido.")
            return
    except ValueError:
        print("Número de pedido inválido.")
        return

    # Associar cliente e funcionário ao pedido
    pedido_selecionado.cliente = cliente_selecionado
    pedido_selecionado.funcionario = funcionario_selecionado

    print(f"Cliente {cliente_selecionado._nome} e funcionário {funcionario_selecionado._nome} associados ao pedido {pedido_selecionado._codigo_pedido} com sucesso.")


def concluir_e_remover_pedido():
    codigo_pedido = input("Digite o código do pedido que deseja concluir: ")

    pedido_encontrado = None
    for pedido in pedidos:
        if pedido._codigo_pedido == codigo_pedido:
            pedido_encontrado = pedido
            pedido.concluir_pedido()

            formas_de_pagamento = escolher_forma_de_pagamento()
            detalhes = input("Informe algum detalhe: ")
            
            nota_fiscal = NotaFiscal(formas_de_pagamento, True, True, detalhes)
            nota_fiscal.display(pedido)

            break

    if pedido_encontrado is None:
        print(f"Pedido {codigo_pedido} não encontrado.")
        return

    pedidos.remove(pedido_encontrado)

    # Check if the order is associated with a table
    for mesa in mesas:
        if pedido_encontrado in mesa._pedidos:
            mesa._pedidos.remove(pedido_encontrado)
            print(f"Pedido {codigo_pedido} concluído e removido da mesa {mesa._numero_da_mesa} com sucesso!")

    print(f"Pedido {codigo_pedido} concluído e removido com sucesso!")

def visualizar_pedidos():
    if not pedidos:
        print("Nenhum pedido cadastrado.")
    else:
        print("Pedidos disponíveis:")
        for i, pedido in enumerate(pedidos):
            print(f"{i + 1}: Código do Pedido - {pedido._codigo_pedido}")

        pedido_numero = input("Digite o número do pedido que deseja visualizar: ")

        try:
            pedido_numero = int(pedido_numero)
            if 1 <= pedido_numero <= len(pedidos):
                print(pedidos[pedido_numero - 1])
            else:
                print("Número de pedido inválido.")
        except ValueError:
            print("Número de pedido inválido. Digite um número válido.")

def adicionar_produto_ao_pedido():
    codigo_pedido = input("Digite o código do pedido ao qual deseja adicionar um produto: ")

    # Find the pedido with the given codigo_pedido
    pedido_encontrado = None
    for pedido in pedidos:
        if pedido._codigo_pedido == codigo_pedido:
            pedido_encontrado = pedido
            break

    if pedido_encontrado is None:
        print(f"Pedido {codigo_pedido} não encontrado.")
        return

    # Get the product code and quantity to add to the pedido
    codigo_produto = input("Digite o código do produto a adicionar: ")
    quantidade = int(input("Digite a quantidade desejada: "))

    # Find the product with the given codigo_produto
    produto_encontrado = encontrar_produto_por_codigo(codigo_produto)

    if produto_encontrado is None:
        print(f"Produto {codigo_produto} não encontrado.")
        return

    # Create an ItemPedido and add it to the pedido
    item_pedido = ItemPedido(produto_encontrado, quantidade)
    pedido_encontrado.adicionar_item_ao_pedido(item_pedido)

    print(f"Produto {produto_encontrado._descricao} adicionado ao pedido {pedido_encontrado._codigo_pedido} com sucesso!")

def selecionar_ou_cadastrar_endereco():
    endereco_entrega = None
    opcao = input("Deseja selecionar um endereço existente (S) ou cadastrar um novo endereço (N)? ").strip().lower()

    if opcao == 's':
        # Selecionar um endereço existente
        if not enderecos:
            print("Nenhum endereço cadastrado. Por favor, cadastre um novo endereço.")
            endereco_entrega = cadastrar_endereco()
        else:
            print("Endereços cadastrados:")
            for i, endereco in enumerate(enderecos):
                print(f"{i + 1}. CEP: {endereco._cep}, Rua: {endereco._rua}, Bairro: {endereco._bairro}, Cidade: {endereco._cidade}")

            escolha = input("Digite o número do endereço desejado: ")
            try:
                escolha_numero = int(escolha)
                if 1 <= escolha_numero <= len(enderecos):
                    endereco_entrega = enderecos[escolha_numero - 1]
                    print("Endereço selecionado com sucesso.")
                else:
                    print("Opção inválida. Usando o endereço padrão.")
                    endereco_entrega = cadastrar_endereco()
            except ValueError:
                print("Opção inválida. Usando o endereço padrão.")
                endereco_entrega = cadastrar_endereco()
    elif opcao == 'n':
        endereco_entrega = cadastrar_endereco()
    else:
        print("Opção inválida. Usando o endereço padrão.")
        endereco_entrega = cadastrar_endereco()

    return endereco_entrega

def cadastrar_endereco():
    cep = input("Digite o CEP do novo endereço: ")
    rua = input("Digite a rua do novo endereço: ")
    numero = input("Digite o número do novo endereço: ")
    complemento = input("Digite o complemento do novo endereço: ")
    bairro = input("Digite o bairro do novo endereço: ")
    cidade = input("Digite a cidade do novo endereço: ")

    novo_endereco = Endereco(cep, rua, numero, complemento, bairro, cidade)
    enderecos.append(novo_endereco)
    print("Novo endereço cadastrado e selecionado com sucesso.")
    return novo_endereco

def cadastrar_mesa():
    numero_da_mesa = input("Digite o número da mesa: ")

    for mesa in mesas:
        if mesa._numero_da_mesa == numero_da_mesa:
            print("Mesa já cadastrada.")
            return

    nova_mesa = Mesa(numero_da_mesa)
    mesas.append(nova_mesa)
    print(f"Mesa {nova_mesa._numero_da_mesa} cadastrada com sucesso!")

if __name__ == '__main__':
    main()