# Importando a biblioteca SQLite
import sqlite3

# Conectando ao banco de dados "expedicoes.db"
conexao = sqlite3.connect("expedicoes.db")
cursor = conexao.cursor()

# ==============================
# 🧪 DESAFIO 1 — LISTAR EQUIPAMENTOS DISPONÍVEIS
# ==============================

# Consulta SQL: seleciona todos os equipamentos com status 'Disponível'
consulta_equipamentos = """
    SELECT * FROM Equipamentos
    WHERE status = 'Disponível';
"""

# Executando a consulta
cursor.execute(consulta_equipamentos)
equipamentos_disponiveis = cursor.fetchall()

# Exibindo os resultados
print("Equipamentos disponíveis para uso:")
for equipamento in equipamentos_disponiveis:
    print(equipamento)

# ==============================
# 🧠 DESAFIO 2 — ESPECIALIDADE MAIS ATIVA EM EXPEDIÇÕES COM COLETA
# ==============================

# Consulta SQL:
# Essa consulta conta quantas vezes cada especialidade participou de expedições
# que coletaram amostras, e seleciona a(s) mais ativa(s)
consulta_especialidade = """
    SELECT p.especialidade, COUNT(*) as total_participacoes
    FROM Pesquisadores p
    JOIN ExpedicaoPesquisador ep ON p.id = ep.pesquisador_id
    JOIN Expedicoes e ON e.id = ep.expedicao_id
    JOIN Amostras a ON a.expedicao_id = e.id
    GROUP BY p.especialidade
    HAVING total_participacoes = (
        SELECT MAX(contagem)
        FROM (
            SELECT COUNT(*) as contagem
            FROM Pesquisadores p2
            JOIN ExpedicaoPesquisador ep2 ON p2.id = ep2.pesquisador_id
            JOIN Expedicoes e2 ON e2.id = ep2.expedicao_id
            JOIN Amostras a2 ON a2.expedicao_id = e2.id
            GROUP BY p2.especialidade
        )
    );
"""

# Executando a consulta
cursor.execute(consulta_especialidade)
resultado_especialidade = cursor.fetchall()

# Mostrando os resultados
print("\nEspecialidade(s) que mais participou(aram) de expedições com coleta de amostras:")
for especialidade, total in resultado_especialidade:
    print(f"- {especialidade} ({total} participação/participações)")

# ==============================
# ✅ Encerrando a conexão
# ==============================
conexao.close()
