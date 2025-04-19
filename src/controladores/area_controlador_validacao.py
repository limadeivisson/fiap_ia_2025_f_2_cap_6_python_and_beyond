from validadores.tipo_validador import validar_string, validar_decimal

def validar_id_area(id):
    try:
        int(id)
        if not id.strip() or len(id.strip()) > 50:
            raise ValueError()
        return None
    except ValueError:
        return "ID inválido!"

def validar_pegar_area_por_id(id):
    return validar_id_area(id)

def validar_criar_area(nome, localizacao, hectar_input):
    if not validar_string(nome) or not nome.strip():
        return "O nome da área não pode estar vazio"

    if not validar_string(localizacao) or not localizacao.strip():
        return "A localização da área não pode estar vazia"
        
    if not hectar_input.strip():
        return "O tamanho em hectares não pode estar vazio"
        
    try:
        hectar = float(hectar_input)
        if not validar_decimal(hectar) or hectar <= 0:
            return "O tamanho em hectares deve ser um número positivo"
    except ValueError:
        return "O tamanho em hectares deve ser um número válido"
    
    return None

def validar_atualizar_area(id, nome, localizacao, hectar_input):
    erro_id = validar_id_area(id)
    if erro_id:
        return erro_id
        
    if not validar_string(nome) or not nome.strip():
        return "O nome da área não pode estar vazio"

    if not validar_string(localizacao) or not localizacao.strip():
        return "A localização da área não pode estar vazia"
        
    if not hectar_input.strip():
        return "O tamanho em hectares não pode estar vazio"
        
    try:
        hectar = float(hectar_input)
        if not validar_decimal(hectar) or hectar <= 0:
            return "O tamanho em hectares deve ser um número positivo"
    except ValueError:
        return "O tamanho em hectares deve ser um número válido"
    
    return None

def validar_deletar_area(id):
    return validar_id_area(id)