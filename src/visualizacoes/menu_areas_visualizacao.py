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
                    print('\n=== Áreas Cadastradas ===\n')
                    areas = pegar_areas()
                    print('\nÁreas Encontradas\n')
                    print(areas)
                case '2':
                    print('\n=== Buscar Área Por ID ===')
                    id = input('\nDigite o ID da área: ')
                    area = pegar_area_por_id(id)
                    print('\nÁrea Encontrada\n')
                    print("ID:", area['id'])
                    print("Nome:", area['nome'])
                    print("Localização:", area['localizacao'])
                    print("Tamanho em hectares:", area['hectar'])
                case '3':
                    print('\n=== Cadastrar Nova Área ===')
                    nome = input('\nDigite o nome da área: ')
                    localizacao = input('\nDigite a localização da área: ')
                    hectar_input = input('\nDigite o tamanho em hectares: ')
                    area = criar_area(nome, localizacao, hectar_input)
                    print('\nÁrea Criada com Sucesso!')
                    print('\nÁrea criada:')
                    print("ID:", area['id'])
                    print("Nome:", area['nome'])
                    print("Localização:", area['localizacao'])
                    print("Tamanho em hectares:", area['hectar'])
                case '4':
                    print('\n=== Alterar Área ===')
                    id = input('\nDigite o ID da área: ')
                    nome = input('\nDigite o novo nome da área: ')
                    localizacao = input('\nDigite a nova localização da área: ')
                    hectar_input = input('\nDigite o novo tamanho em hectares: ')
                    area = atualizar_area_por_id(id, nome, localizacao, hectar_input)
                    print('\nÁrea atualizada com sucesso!')
                    print('\nÁrea atualizada:')
                    print("ID:", area['id'])
                    print("Nome:", area['nome'])
                    print("Localização:", area['localizacao'])
                    print("Tamanho em hectares:", area['hectar'])
                case '5':
                    print('\n=== Deletar Área ===')
                    id = input('\nDigite o ID da área: ')
                    deletar_area_por_id(id)
                    print('\nÁrea deletada com sucesso!')
                case '0':
                    print('\nSaindo do menu de áreas...')
                    break
                case _:
                    raise Exception("Opção inválida!")
        except Exception as e:
            os.system("cls")
            print(f'\nERRO')
            print(f'\n\033[31m{str(e)}\033[0m')
        finally:
            input("\n\nPressione ENTER")