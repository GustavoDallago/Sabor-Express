import os

restaurantes = [{'nome':'Pizza Superma', 'categoria':'Italiana','ativo':False},
                {'nome':'Sushi', 'categoria':'Japonesa','ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    '''Essa função é responsável por exibir o nome do programa "Sabor express"'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes(): 
    '''Essa função exibe as opções de escolha para o usuário'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar restaurante')
    print('4. Sair\n')

def finalizar_app(): 
    '''Essa função é responsável por finalizar o aplicativo'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal(): 
    '''Essa função é responsável por toda vez que você finaliza uma etapa voltar para o menu principal'''
    input('\nDigite ENTER para voltar ao menu ')
    main()

def opcao_invalida(): 
    '''essa função é responsável por não deixar o usuário escrever qualquer coisa que não tenha nexo com o programa'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto): 
    '''essa função é responsável pelos prints'''
    os.system('cls')
    linha = '*' * (len(texto) + 2)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante(): 
    '''essa função é responsável por cadastrar os restaurantes no dicionário'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    resposta = input('Quer cadastrar um novo restaurante? (S/N) ')
    if resposta.upper() == "S":
        cadastrar_novo_restaurante()
    else:
        voltar_ao_menu_principal()

def listar_restaurantes(): 
    '''Essa função mostra todos os restaurantes'''
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alterar_estado_restaurante(): 
    '''Essa função altera o estado para ativo ou desativado'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
      print('O restaurante não foi encontrado')
    voltar_ao_menu_principal() 

def escolher_opcao(): 
    '''Essa função armazena e direciona a escolha do usuário'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

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

def main(): 
    '''essa função roda o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()