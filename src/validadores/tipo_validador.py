def validar_string(valor):
    try:
        return isinstance(valor, str)
    except Exception as e:
        print(f"Erro ao validar string: {str(e)}")
        return False

def validar_inteiro(valor):
    try:
        return isinstance(valor, int)
    except Exception as e:
        print(f"Erro ao validar inteiro: {str(e)}")
        return False

def validar_decimal(valor):
    try:
        return isinstance(valor, float)
    except Exception as e:
        print(f"Erro ao validar decimal: {str(e)}")
        return False

def validar_booleano(valor):
    try:
        return isinstance(valor, bool)
    except Exception as e:
        print(f"Erro ao validar booleano: {str(e)}")
        return False

def validar_lista(valor):
    try:
        return isinstance(valor, list)
    except Exception as e:
        print(f"Erro ao validar lista: {str(e)}")
        return False