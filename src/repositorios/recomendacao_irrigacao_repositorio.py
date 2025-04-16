from config.db.db_config import pegar_conexao

def pegar():
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM recomendacao_irrigacao')
        recomendacoes = cursor.fetchall()
        return recomendacoes
    except Exception as e:
        print(f"Erro ao buscar recomendações de irrigação: {str(e)}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def pegar_por_id(id):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM recomendacao_irrigacao WHERE id = :1', [id])
        recomendacao = cursor.fetchone()
        return recomendacao
    except Exception as e:
        print(f"Erro ao buscar recomendação de irrigação por ID: {str(e)}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def criar(irrigacao_id, status, feedback):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'INSERT INTO recomendacao_irrigacao (irrigacao_id, status, feedback) VALUES (:1, :2, :3) RETURNING id INTO :4',
            [irrigacao_id, status, feedback, cursor.var(int)]
        )
        id = cursor.var.getvalue()
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao criar recomendação de irrigação: {str(e)}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def atualizar_por_id(id, irrigacao_id, status, feedback):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE recomendacao_irrigacao SET irrigacao_id = :1, status = :2, feedback = :3 WHERE id = :4',
            [irrigacao_id, status, feedback, id]
        )
        conexao.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar recomendação de irrigação: {str(e)}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def deletar_por_id(id):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM recomendacao_irrigacao WHERE id = :1', [id])
        conexao.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao deletar recomendação de irrigação: {str(e)}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()