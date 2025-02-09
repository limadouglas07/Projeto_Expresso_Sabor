import os  # Essa biblioteca serve para limpar o terminal...

# Adicionamos uma lista para o cadastro dos restaurantes, com o uso de dicionários.
restaurantes = [{'nome': 'Praça', 'categoria': 'Japoneza', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizzaria', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]


def exibir_nome_do_programa():

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)  # Aspas triplas para pular linhas..


def exibir_opcoes():
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurantes')
    print('3. Alternar Status dos Restaurantes')
    print('4. Sair \n')

# Função é um bloco de código que vai realizar uma determinada ação, nesse caso é finalizar o app.


def finalizar_app():  # Serve para limpar o terminal windows.
    exibir_subtitulo('Finalizando o app')


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar a opção principal:')
    main()


def opcao_invalida():
    print('Opção Inválida! \n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''
    Essa função é responsável por cadastrar um novo restaurante no app.
       Inputs:
       - Nome do Restaurante
       - Categoria
       Outputs:
       - Adiciona um novo restaurante a lista de restaurantes. 

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(
        f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        # Aplica o ternário no caso abaixo.
        ativo = 'ativado'if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()


def alterar_estado_restaurante():
    exibir_subtitulo('Alterando o Status do restaurante')
    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o Status: Ativo ou Desativo:')
    # vai ser falso porque não encontrei ainda o restaurante.
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            # invertendo o Status do restaurante.
            restaurante['ativo'] = not restaurante['ativo']
            # Abaixo estaremos fazendo um ternário.
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante[
                'ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        print(f'Você escolheu a opção:{opcao_escolhida}')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():  # Essa função é o passo a passo para que o programa funcione.
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':  # Arquivo principal
    main()
