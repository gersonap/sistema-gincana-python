import sqlite3
class Equipe:
    def __init__(self, nome, lider, ano_fundacao, qtde_membros, pontuacao):
        self.nome = nome
        self.lider = lider
        self.ano_fundacao = int(ano_fundacao)
        self.qtde_membros = int(qtde_membros)
        self.idade = 2026 - self.ano_fundacao
        # self.pontuacao_inicial = self.qtde_membros * 50
        self.__pontuacao = pontuacao

    def registrar_pontuacao(self, valor):
        self.__pontuacao += valor

    def aplicar_penalidade(self, valor):
        self.__pontuacao -= valor

    def verificar_qualificacao(self):
        if self.qtde_membros >= 5:
            return "#### EQUIPE Qualificada!"
        else:
            return "#### EQUIPE Não Qualificada!"
    @property
    def pontuacao(self):
        return self.__pontuacao 

while True:
    # Este programa solicita ao usuário informações sobre uma equipe e exibe essas informações na tela.
    nome_equipe = input("Digite o nome da equipe: ")
    nome_lider = input("Digite o nome do líder da equipe: ")
    ano_fundacao = input("Digite o ano de fundação da equipe: ")
    qtde_membros = int(input("Digite a quantidade de membros da equipe: "))
    pontuacao = int(input("Digite a pontuação inicial da equipe: "))
    nova_equipe = Equipe(nome_equipe, nome_lider, ano_fundacao, qtde_membros, pontuacao)
    
    # conectando ao banco de dados SQLite
    conexao = sqlite3.connect('gincana.db')
    cursor = conexao.cursor()
    # inserindo os dados da equipe na tabela
    cursor.execute("""INSERT INTO equipes (nome, lider, ano_fundacao, qtde_membros, pontuacao) VALUES (?, ?, ?, ?, ?)""", 
                   (nova_equipe.nome, nova_equipe.lider, nova_equipe.ano_fundacao, nova_equipe.qtde_membros, nova_equipe.pontuacao))
    # salvando as alterações no banco de dados
    conexao.commit()
    # fechando a conexão com o banco de dados
    conexao.close()
    
    print("\nInformações da equipe cadastrada:")

    # Exibe as informações fornecidas pelo usuário
    print(f"-- O nome da sua equipe é: {nome_equipe}")
    print(f"-- Nome do líder de sua equipe é: {nome_lider}")
    print(f"-- Ano de fundação da sua equipe é: {ano_fundacao}")
    print(f"-- Sua equipe tem {nova_equipe.idade} anos de existência")
    print(f"-- A quantidade de membros da sua equipe é: {qtde_membros}")
    print(f"-------: A pontuação inicial da sua equipe é: {nova_equipe.pontuacao} pontos")
    print()
    continuar = input("Deseja cadastrar outra equipe? (s/n): ")
    if continuar.upper() == 'N':
        break
print("--- FIM DO PROCESSO DE CREDENCIAMENTO ---")
print("### Programa finalizado!")
print()
print()
print("\n--- EQUIPES SALVAS NO BANCO DE DADOS ---")

# conectando ao banco de dados SQLite para realizar a consulta
conexao = sqlite3.connect('gincana.db')
cursor = conexao.cursor()
# realizando a consulta para obter todas as equipes cadastradas
cursor.execute("SELECT * FROM equipes")
# obtendo os resultados da consulta
equipes = cursor.fetchall()
# exibindo as informações de cada equipe cadastrada
for linha in equipes:
    print(linha)
    #print(f"ID: {linha[0]}, Nome: {linha[1]}, Líder: {linha[2]}, Ano de Fundação: {linha[3]}, Quantidade de Membros: {linha[4]}, Pontuação: {linha[5]}")

# fechando a conexão com o banco de dados
conexao.close()
