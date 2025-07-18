import sqlite3

# Conectando ou criando o banco
conexao = sqlite3.connect("expedicoes.db")
cursor = conexao.cursor()

# Apagar tabelas antigas se existirem (evita conflito)
cursor.executescript("""
DROP TABLE IF EXISTS Equipamentos;
DROP TABLE IF EXISTS Pesquisadores;
DROP TABLE IF EXISTS Expedicoes;
DROP TABLE IF EXISTS Amostras;
DROP TABLE IF EXISTS ExpedicaoPesquisador;
""")

# Criando todas as tabelas
cursor.executescript("""
CREATE TABLE Equipamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    descricao TEXT,
    status TEXT
);

CREATE TABLE Pesquisadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    especialidade TEXT
);

CREATE TABLE Expedicoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    local TEXT
);

CREATE TABLE Amostras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    expedicao_id INTEGER,
    FOREIGN KEY (expedicao_id) REFERENCES Expedicoes(id)
);

CREATE TABLE ExpedicaoPesquisador (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pesquisador_id INTEGER,
    expedicao_id INTEGER,
    FOREIGN KEY (pesquisador_id) REFERENCES Pesquisadores(id),
    FOREIGN KEY (expedicao_id) REFERENCES Expedicoes(id)
);
""")

# Inserindo dados de exemplo
cursor.executescript("""
INSERT INTO Equipamentos (nome, descricao, status) VALUES
('Microscópio', 'Ampliação de amostras', 'Disponível'),
('GPS', 'Localização de campo', 'Em uso'),
('Bússola', 'Orientação geográfica', 'Disponível');

INSERT INTO Pesquisadores (nome, especialidade) VALUES
('Ana', 'Biologia'),
('Carlos', 'Geologia'),
('Fernanda', 'Química');

INSERT INTO Expedicoes (data, local) VALUES
('2024-01-15', 'Floresta Amazônica'),
('2024-02-20', 'Pantanal'),
('2024-03-05', 'Cerrado');

INSERT INTO Amostras (tipo, expedicao_id) VALUES
('Solo', 1),
('Água', 1),
('Rocha', 2),
('Planta', 3);

INSERT INTO ExpedicaoPesquisador (pesquisador_id, expedicao_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(2, 3),
(3, 1);
""")

# Finalizando
conexao.commit()
conexao.close()

print("Banco de dados recriado com sucesso!")
