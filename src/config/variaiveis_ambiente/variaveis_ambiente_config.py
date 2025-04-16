import json
import os

def pegar_variaveis_ambiente():
    diretorio_atual = os.path.dirname(__file__)
    json_path = os.path.join(diretorio_atual, "variaveis_ambiente.json")
    with open(json_path, "r") as file:
        variaveis_ambiente = file.read()
        return json.loads(variaveis_ambiente)
    
def pegar_oracle_db_usuario():
    pegar_variaveis = pegar_variaveis_ambiente()
    return pegar_variaveis['oracle_db_usuario']

def pegar_oracle_db_senha():
    pegar_variaveis = pegar_variaveis_ambiente()
    return pegar_variaveis['oracle_db_senha']
