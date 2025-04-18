from controladores.plantio_controlador import pegar_plantios, pegar_plantio_por_id, criar_plantio, atualizar_plantio_por_id, deletar_plantio_por_id
import os

def exibir_menu_principal():
    print('\n=== Menu Plantio ===\n')
    print('1. Listar todos os plantios')
    print('2. Buscar plantio por ID')
    print('3. Criar novo plantio')
    print('4. Atualizar plantio')
    print('5. Deletar plantio')
    print('0. Sair')
    print('\nEscolha uma opção: ', end='')

def menu_plantios():
    while True:
        try:
            os.system("cls")
            exibir_menu_principal()
            opcao = input().strip()
            os.system("cls")
            match opcao:
                case '1':
                    pegar_plantios()
                case '2':
                    id = input('\nDigite o ID do plantio: ')
                    pegar_plantio_por_id(id)
                case '3':
                    area_id = input('\nDigite o ID da área: ')
                    cultura_id = input('\nDigite o ID da cultura: ')
                    data_plantio = input('\nDigite a data do plantio (YYYY-MM-DD): ')
                    criar_plantio(area_id, cultura_id, data_plantio)
                case '4':
                    id = input('\nDigite o ID do plantio: ')
                    area_id = input('\nDigite o novo ID da área: ')
                    cultura_id = input('\nDigite o novo ID da cultura: ')
                    data_plantio = input('\nDigite a nova data do plantio (YYYY-MM-DD): ')
                    atualizar_plantio_por_id(id, area_id, cultura_id, data_plantio)
                case '5':
                    id = input('\nDigite o ID do plantio: ')
                    deletar_plantio_por_id(id)
                case '0':
                    print('\nSaindo do menu de plantios...')
                    break
                case _:
                    print('\nOpção inválida! Por favor, escolha uma opção válida de plantios.')
        except Exception as e:
            print(f'\nErro: {str(e)}')
            print('Por favor, tente novamente.')
        finally:
            input("\nPressione ENTER")