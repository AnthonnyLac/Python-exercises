# Declarando variáveis globais
campos_obrigatorios = []
banco_usuarios = []

def cadastrar_usuario(campos_obrigatorios):
    """
    Cadastra um usuario com campos obrigatórios e campos adicionais opcionais
    Retorna o dicionario do usuário
    """
    usuario = {}
    for campo in campos_obrigatorios:
        valor = input(f'Digite o valor para o campo {campo}: ')
        usuario[campo] = valor

    while True:
        campoExtra = input('Digite um campo extra ou escreva [sair] para finalizar: ')
        if campoExtra.lower() == 'sair':
            break
        valorExtra = input(f'Digite o valor para o campo {campoExtra}: ')
        usuario[campoExtra] = valorExtra

    banco_usuarios.append(usuario)
    return usuario

def imprimir_usuarios(*args, **kwargs):
    """
    Imprime informacões de usuarios.
    """
    if not args and not kwargs:
        for usuario in banco_usuarios:
            print(usuario)
    elif args:
        for nome in args:
            for usuario in banco_usuarios:
                if nome in usuario:
                    print(usuario)
    elif kwargs:
        filteredUsers = []
        for usuario in banco_usuarios:
            satisfiesConditions = True
            for campo, valor in kwargs.items():
                if campo not in usuario or usuario[campo] != valor:
                    satisfiesConditions = False
                    break
            if satisfiesConditions:
                filteredUsers.append(usuario)
        for usuario in filteredUsers:
            print(usuario)

def main():
    global campos_obrigatorios

    print("Bem vindo ao Banco de Usuarios!")

    while True:
        print("\nMenu:")
        print("1 - Cadastrar usuario.")
        print("2 - Imprimir usuarios.")
        print("exit - para sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            campos_obrigatorios = input("Digite os campos obrigatórios os separando por vírgula: ").split(',')
            usuario = cadastrar_usuario(campos_obrigatorios)
            print("Usuário cadastrado com sucesso.")
            print(usuario)
        elif opcao == "2":
            print("\nOpções:")
            print("1 - Imprimir todos")
            print("2 - Filtrar por nomes")
            print("3 - Filtrar por campos")
            print("4 - Filtrar por nomes e campos")
            subOpcao = input("Escolha uma opção de impressão: ")

            if subOpcao == "1":
                imprimir_usuarios()
            elif subOpcao == "2":
                nomes = input("Digite os nomes separados por virgula: ").split(',')
                imprimir_usuarios(*nomes)
            elif subOpcao == "3":
                campos = input("Digite os campos de busca separados por virgula: ").split(',')
                kwargs = {}
                for campo in campos:
                    valor = input(f'Digite o valor para o campo {campo}: ')
                    kwargs[campo] = valor
                imprimir_usuarios(**kwargs)
            elif subOpcao == "4":
                nomes = input("Digite os nomes separados por virgula: ").split(',')
                campos = input("Digite os campos de busca separados por virgula: ").split(',')
                kwargs = {}
                for campo in campos:
                    valor = input(f'Digite o valor para o campo {campo}: ')
                    kwargs[campo] = valor
                imprimir_usuarios(*nomes, **kwargs)
        elif opcao == "exit":
            print("Finalizando programa")
            break
        else:
            print("Opção invalida")

if __name__ == "__main__":
    main()
