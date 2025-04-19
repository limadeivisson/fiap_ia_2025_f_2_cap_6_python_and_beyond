from config.db.db_config import pegar_conexao

def pegar():
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT i.id, i.plantio_id, p.nome as plantio_nome, i.data_irrigacao, i.volume_agua_l
            FROM irrigacao i
            JOIN plantio p ON i.plantio_id = p.id
        ''')
        irrigacoes = cursor.fetchall()
        return irrigacoes
    except Exception as e:
        print(f"Erro ao buscar irrigações: {str(e)}")
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
        cursor.execute('''
            SELECT i.id, i.plantio_id, p.nome as plantio_nome, i.data_irrigacao, i.volume_agua_l
            FROM irrigacao i
            JOIN plantio p ON i.plantio_id = p.id
            WHERE i.id = :1
        ''', [id])
        irrigacao = cursor.fetchone()
        return irrigacao
    except Exception as e:
        print(f"Erro ao buscar irrigação por ID: {str(e)}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def criar(plantio_id, data_irrigacao, volume_agua_l):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        id_var = cursor.var(int)
        cursor.execute(
            'INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (:1, :2, :3) RETURNING id INTO :4',
            [plantio_id, data_irrigacao, volume_agua_l, id_var]
        )
        id = id_var.getvalue()
        conexao.commit()
        return id
    except Exception as e:
        print(f"Erro ao criar irrigação: {str(e)}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def atualizar_por_id(id, plantio_id, data_irrigacao, volume_agua_l):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE irrigacao SET plantio_id = :1, data_irrigacao = :2, volume_agua_l = :3 WHERE id = :4',
            [plantio_id, data_irrigacao, volume_agua_l, id]
        )
        conexao.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar irrigação: {str(e)}")
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
        cursor.execute('DELETE FROM irrigacao WHERE id = :1', [id])
        conexao.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao deletar irrigação: {str(e)}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()