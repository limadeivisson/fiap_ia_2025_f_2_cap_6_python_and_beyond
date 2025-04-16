from config.db.db_config import pegar_conexao

def pegar():
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM cultura')
        culturas = cursor.fetchall()
        return culturas
    except Exception as e:
        print(f"Erro ao buscar culturas: {str(e)}")
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
        cursor.execute('SELECT * FROM cultura WHERE id = :1', [id])
        cultura = cursor.fetchone()
        return cultura
    except Exception as e:
        print(f"Erro ao buscar cultura por ID: {str(e)}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def criar(nome, coeficiente_kc, profundidade_raiz_cm, consumo_hidrico_diario_l_m2):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'INSERT INTO cultura (nome, coeficiente_kc, profundidade_raiz_cm, consumo_hidrico_diario_l_m2) VALUES (:1, :2, :3, :4) RETURNING id INTO :5',
            [nome, coeficiente_kc, profundidade_raiz_cm, consumo_hidrico_diario_l_m2, cursor.var(int)]
        )
        id = cursor.var.getvalue()
        conexao.commit()
        return True
    except Exception as e:
        print(f"Erro ao criar cultura: {str(e)}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def atualizar_por_id(id, nome, coeficiente_kc, profundidade_raiz_cm, consumo_hidrico_diario_l_m2):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE cultura SET nome = :1, coeficiente_kc = :2, profundidade_raiz_cm = :3, consumo_hidrico_diario_l_m2 = :4 WHERE id = :5',
            [nome, coeficiente_kc, profundidade_raiz_cm, consumo_hidrico_diario_l_m2, id]
        )
        conexao.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar cultura: {str(e)}")
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
        cursor.execute('DELETE FROM cultura WHERE id = :1', [id])
        conexao.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao deletar cultura: {str(e)}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()