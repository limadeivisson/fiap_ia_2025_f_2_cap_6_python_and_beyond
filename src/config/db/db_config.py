import oracledb
from config.variaiveis_ambiente.variaveis_ambiente_config import pegar_oracle_db_usuario, pegar_oracle_db_senha

def pegar_conexao():
    return oracledb.connect(
        user=pegar_oracle_db_usuario(),
        password=pegar_oracle_db_senha(),
        dsn="oracle.fiap.com.br:1521/ORCL"
    )
