
def cadastrar_funcionario():
    id = input("Digite o ID do funcionário: ")
    nome = input("Digite o nome do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    email = input("Digite o email do funcionário: ")
    senha = input("Digite a senha do funcionário: ")

    novo_funcionario = Funcionario.cadastrar_funcionario(id, nome, cpf, email, senha)
    print(f"Funcionário {novo_funcionario._id} cadastrado com sucesso!")