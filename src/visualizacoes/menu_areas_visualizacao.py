from controladores.area_controlador import pegar_areas, pegar_area_por_id, criar_area, atualizar_area_por_id, deletar_area_por_id
import os

def exibir_menu_princiap():
    print('\n=== Menu Área ===\n')
    print('1. Listar todas as áreas')
    print('2. Buscar área por ID')
    print('3. Criar nova área')
    print('4. Atualizar área')
    print('5. Deletar área')
    print('0. Sair')
    print('\nEscolha uma opção: ', end='')

def menu_areas():
    while True:
        try:
            os.system("cls")
            exibir_menu_princiap()
            opcao = input().strip()
            os.system("cls")
            match opcao:
                case '1':
                    pegar_areas()
                case '2':
                    print('\n=== Buscar Área ===')
                    id = input('\nDigite o ID da área: ')
                    pegar_area_por_id(id)
                case '3':
                    print('\n=== Cadastrar Nova Área ===')
                    nome = input('\nDigite o nome da área: ')
                    localizacao = input('\nDigite a localização da área: ')
                    hectar_input = input('\nDigite o tamanho em hectares: ')
                    criar_area(nome, localizacao, hectar_input)
                case '4':
                    print('\n=== Alterar Área ===')
                    id = input('\nDigite o ID da área: ')
                    nome = input('\nDigite o novo nome da área: ')
                    localizacao = input('\nDigite a nova localização da área: ')
                    hectar_input = input('\nDigite o novo tamanho em hectares: ')
                    atualizar_area_por_id(id, nome, localizacao, hectar_input)
                case '5':
                    print('\n=== Deletar Área ===')
                    id = input('\nDigite o ID da área: ')
                    deletar_area_por_id(id)
                case '0':
                    print('\nSaindo do menu de áreas...')
                    break
                case _:
                    os.system("cls")
                    print('\nOpção inválida!')
                    print('\nPor favor, escolha uma opção válida.')
        except Exception as e:
            print(f'\nErro: {str(e)}')
            print('\nPor favor, tente novamente.')
        finally:
            input("\nPressione ENTER")