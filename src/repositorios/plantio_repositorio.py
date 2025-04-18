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

def criar(area_id, cultura_id, data_plantio):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        id_var = cursor.var(int)
        cursor.execute(
            'INSERT INTO plantio (area_id, cultura_id, data_plantio) VALUES (:1, :2, :3) RETURNING id INTO :4',
            [area_id, cultura_id, data_plantio, id_var]
        )
        id = id_var.getvalue()
        conexao.commit()
        return id
    except Exception as e:
        print(f"Erro ao criar plantio: {str(e)}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def atualizar_por_id(id, area_id, cultura_id, data_plantio):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE plantio SET area_id = :1, cultura_id = :2, data_plantio = :3 WHERE id = :4',
            [area_id, cultura_id, data_plantio, id]
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