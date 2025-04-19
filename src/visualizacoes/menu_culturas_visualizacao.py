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
                    print('\n=== Áreas Culturas ===\n')
                    culturas = pegar_culturas()
                    print('\nCulturas Encontradas\n')
                    print(culturas)
                case '2':
                    print('\n=== Buscar Cultura Por ID ===')
                    id = input('\nDigite o ID da cultura: ')
                    cultura = pegar_cultura_por_id(id)
                    print('\nCulturas Encontrada\n')
                    print("ID:", cultura["id"])
                    print("Nome:", cultura["nome"])
                    print("Consumo Hídrico Diário (L/m²):", cultura["consumo_hidrico_diario_l_m2"])
                case '3':
                    print('\n=== Cadastrar Nova Cultura ===')
                    nome = input('\nDigite o nome da cultura: ')
                    consumo_hidrico = input('\nDigite o consumo hídrico diário (L/m²): ')
                    cultura = criar_cultura(nome, consumo_hidrico)
                    print('\nCultura Criada com Sucesso!')
                    print('\nCultura criada:')
                    print("ID:", cultura["id"])
                    print("Nome:", cultura["nome"])
                    print("Consumo Hídrico Diário (L/m²):", cultura["consumo_hidrico_diario_l_m2"])
                case '4':
                    print('\n=== Alterar Cultura ===')
                    id = input('\nDigite o ID da cultura: ')
                    nome = input('\nDigite o novo nome da cultura: ')
                    consumo_hidrico = input('\nDigite o novo consumo hídrico diário (L/m²): ')
                    cultura = atualizar_cultura_por_id(id, nome, consumo_hidrico)
                    print('\nCultura atualizada com sucesso!')
                    print('\nCultura atualizada:')
                    print("ID:", cultura["id"])
                    print("Nome:", cultura["nome"])
                    print("Consumo Hídrico Diário (L/m²):", cultura["consumo_hidrico_diario_l_m2"])
                case '5':
                    print('\n=== Deletar Cultura ===')
                    id = input('\nDigite o ID da cultura: ')
                    deletar_cultura_por_id(id)
                    print('\nCultura deletada com sucesso!')
                case '0':
                    print('\nSaindo do menu de culturas...')
                    break
                case _:
                    raise Exception("Opção inválida!")
        except Exception as e:
            os.system("cls")
            print(f'\nERRO')
            print(f'\n\033[31m{str(e)}\033[0m')
        finally:
            input("\nPressione ENTER")