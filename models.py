from database import conectar

def criar_materia(nome, confianca_geral):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO materias (nome, confianca_geral) VALUES (%s, %s)",
        (nome, confianca_geral)
    )
    conn.commit()
    conn.close()
    print("Matéria criada!")

def criar_atividade(materia_id, titulo, data_limite, peso, confianca, horario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO atividades (materia_id, titulo, data_limite, peso, confianca, horario) VALUES (%s, %s, %s, %s, %s, %s)",
        (materia_id, titulo, data_limite, peso, confianca, horario)
    )
    conn.commit()
    conn.close()
    print("Atividade criada!")

def listar_atividades_pendentes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM atividades WHERE status = 'pendente'")
    atividades = cursor.fetchall()
    conn.close()
    return atividades

def marcar_concluida(atividade_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE atividades SET status = 'concluida' WHERE id = %s",
        (atividade_id,)
    )
    conn.commit()
    conn.close()
    print("Atividade marcada como concluída!")