from config.db.db_config import pegar_conexao

def pegar():
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM plantio')
        plantios = cursor.fetchall()
        return plantios
    except Exception as e:
        print(f"Erro ao buscar plantios: {str(e)}")
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
        cursor.execute('SELECT * FROM plantio WHERE id = :1', [id])
        plantio = cursor.fetchone()
        return plantio
    except Exception as e:
        print(f"Erro ao buscar plantio por ID: {str(e)}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def criar(area_id, cultura_id, data_plantio, fase_atual):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'INSERT INTO plantio (area_id, cultura_id, data_plantio, fase_atual) VALUES (:1, :2, :3, :4) RETURNING id INTO :5',
            [area_id, cultura_id, data_plantio, fase_atual, cursor.var(int)]
        )
        id = cursor.var.getvalue()
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao criar plantio: {str(e)}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def atualizar_por_id(id, area_id, cultura_id, data_plantio, fase_atual):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE plantio SET area_id = :1, cultura_id = :2, data_plantio = :3, fase_atual = :4 WHERE id = :5',
            [area_id, cultura_id, data_plantio, fase_atual, id]
        )
        conexao.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar plantio: {str(e)}")
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
        cursor.execute('DELETE FROM plantio WHERE id = :1', [id])
        conexao.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao deletar plantio: {str(e)}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()