# Criando o banco de dados SQLite e a tabela de equipes
import sqlite3

# 1. Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('gincana.db')

# 2. Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# 3. Criar a tabela de equipes, se não existir
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS equipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    lider TEXT NOT NULL,
    ano_fundacao INTEGER NOT NULL,
    qtde_membros INTEGER NOT NULL,  
    pontuacao INTEGER DEFAULT 0
     )
""")

# 4. Salvar (commit) as alterações e fechar a conexão
conexao.commit()
conexao.close()
