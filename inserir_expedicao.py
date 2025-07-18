import sqlite3

conexao = sqlite3.connect("expedicoes.db")
cursor = conexao.cursor()

# Dados da nova expedição
titulo_expedicao = "Expedição vulcao Villarrica"
local = "39°25' S, 71°56' W"
data_inicio = "2025-07-01"  # vamos usar só um campo data para simplificar
data_fim = "2025-07-04"  # Não existe campo fim na tabela, ignoramos

# Pesquisadores e seus nomes (sem papéis, pois banco não suporta)
pesquisadores = [
    "Dr. Gabriel Alves",  # coordenador
    "Ana Julia Câmara",
    "Guilherme Silveira"
]

# Amostra coletada
amostra_tipo = "AR"
resultado_analise = "concentração elevada de compostos de enxofre, sendo o dióxido de enxofre (SO2) um dos principais poluentes"
# OBS: banco não tem campo resultado, então podemos guardar isso no campo tipo ou ignorar

try:
    # Inserir expedição (local + data)
    cursor.execute("INSERT INTO Expedicoes (local, data) VALUES (?, ?)", (local, data_inicio))
    conexao.commit()

    # Pegar id da expedição inserida
    expedicao_id = cursor.lastrowid

    # Inserir pesquisadores se não existirem e pegar seus IDs
    pesquisador_ids = []
    for nome in pesquisadores:
        cursor.execute("SELECT id FROM Pesquisadores WHERE nome = ?", (nome,))
        res = cursor.fetchone()
        if res:
            pesquisador_ids.append(res[0])
        else:
            cursor.execute("INSERT INTO Pesquisadores (nome, especialidade) VALUES (?, ?)", (nome, "Desconhecida"))
            conexao.commit()
            pesquisador_ids.append(cursor.lastrowid)

    # Relacionar pesquisadores com expedição
    for pid in pesquisador_ids:
        cursor.execute("INSERT INTO ExpedicaoPesquisador (pesquisador_id, expedicao_id) VALUES (?, ?)", (pid, expedicao_id))
    conexao.commit()

    # Inserir amostra associada à expedição
    cursor.execute("INSERT INTO Amostras (tipo, expedicao_id) VALUES (?, ?)", (amostra_tipo, expedicao_id))
    conexao.commit()

    print("Expedição e dados inseridos com sucesso!")

except Exception as e:
    print("Erro ao inserir dados:", e)

finally:
    conexao.close()
