from controladores.cultura_controlador import pegar_culturas, pegar_cultura_por_id, criar_cultura, atualizar_cultura_por_id, deletar_cultura_por_id
import os

def exibir_menu_principal():
    print('\n=== Menu Cultura ===\n')
    print('1. Listar todas as culturas')
    print('2. Buscar cultura por ID')
    print('3. Criar nova cultura')
    print('4. Atualizar cultura')
    print('5. Deletar cultura')
    print('0. Sair')
    print('\nEscolha uma opção: ', end='')

def menu_culturas():
    while True:
        try:
            os.system("cls")
            exibir_menu_principal()
            opcao = input().strip()
            os.system("cls")
            match opcao:
                case '1':
                    pegar_culturas()
                case '2':
                    id = input('\nDigite o ID da cultura: ')
                    pegar_cultura_por_id(id)
                case '3':
                    nome = input('\nDigite o nome da cultura: ')
                    consumo_hidrico = input('\nDigite o consumo hídrico diário (L/m²): ')
                    criar_cultura(nome, consumo_hidrico)
                case '4':
                    id = input('\nDigite o ID da cultura: ')
                    nome = input('\nDigite o novo nome da cultura: ')
                    consumo_hidrico = input('\nDigite o novo consumo hídrico diário (L/m²): ')
                    atualizar_cultura_por_id(id, nome, consumo_hidrico)
                case '5':
                    id = input('\nDigite o ID da cultura: ')
                    deletar_cultura_por_id(id)
                case '0':
                    print('\nSaindo do menu de culturas...')
                    break
                case _:
                    print('\nOpção inválida! Por favor, escolha uma opção válida de culturas.')
        except Exception as e:
            print(f'\nErro: {str(e)}')
            print('Por favor, tente novamente.')
        finally:
            input("\nPressione ENTER")