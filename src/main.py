from visualizacoes.menu_areas_visualizacao import menu_areas
import os

def exibir_menu():
    print('\n=== Menu Principal ===\n')
    print('1. Áreas')
    print('0. Sair')
    print('\nEscolha uma opção: ', end='')


def main():
    while True:
        try:
            os.system("cls")
            exibir_menu()
            opcao = input().strip()
            match opcao:
                case '1':
                    menu_areas()
                case '0':
                    print('\nSaindo do sistema...')
                    break
                case _:
                    print('\nOpção inválida! Por favor, escolha uma opção válida.')
        except Exception as e:
            print(f'\nErro: {str(e)}')
            print('Por favor, tente novamente.')

main()