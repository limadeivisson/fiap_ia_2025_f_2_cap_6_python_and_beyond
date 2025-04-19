from config.db.db_config import pegar_conexao

def pegar():
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT p.id, p.nome, p.observacao, p.area_id, a.nome as area_nome, p.cultura_id, c.nome as cultura_nome, p.data_plantio
            FROM plantio p
            JOIN area a ON p.area_id = a.id
            JOIN cultura c ON p.cultura_id = c.id
        ''')
        plantios = cursor.fetchall()
        return plantios
    except Exception as e:
        raise Exception(f"Erro ao buscar plantios: {str(e)}")
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
            SELECT p.id, p.nome, p.observacao, p.area_id, a.nome as area_nome, p.cultura_id, c.nome as cultura_nome, p.data_plantio
            FROM plantio p
            JOIN area a ON p.area_id = a.id
            JOIN cultura c ON p.cultura_id = c.id
            WHERE p.id = :1
        ''', [id])
        plantio = cursor.fetchone()
        return plantio
    except Exception as e:
        raise Exception(f"Erro ao buscar plantio por ID: {str(e)}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def criar(nome, observacao, area_id, cultura_id, data_plantio):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        id_var = cursor.var(int)
        cursor.execute(
            'INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES (:1, :2, :3, :4, :5) RETURNING id INTO :6',
            [nome, observacao, area_id, cultura_id, data_plantio, id_var]
        )
        id = id_var.getvalue()
        conexao.commit()
        return id
    except Exception as e:
        raise Exception(f"Erro ao criar plantio: {str(e)}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def atualizar_por_id(id, nome, observacao, area_id, cultura_id, data_plantio):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE plantio SET nome = :1, observacao = :2, area_id = :3, cultura_id = :4, data_plantio = :5 WHERE id = :6',
            [nome, observacao, area_id, cultura_id, data_plantio, id]
        )
        conexao.commit()
        return cursor.rowcount > 0
    except Exception as e:
        raise Exception(f"Erro ao atualizar plantio: {str(e)}")
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
        raise Exception(f"Erro ao deletar plantio: {str(e)}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()