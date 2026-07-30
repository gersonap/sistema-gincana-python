import sqlite3
# conectando ao banco de dados SQLite
conexao = sqlite3.connect('gincana.db')
cursor = conexao.cursor()
cursor.execute("""SELECT * FROM equipes""")
equipes = cursor.fetchall()
for linha in equipes:
    print(f"-- ID: {linha[0]} | Nome da equipe: {linha[1]} | Nome do líder: {linha[2]} | Ano de fundação: {linha[3]} | Quantidade de membros: {linha[4]} | Pontuação: {linha[5]}")
print("--- FIM DA LISTA ---")
# processo de atualização de pontuação
while True:
    opcao = input("Deseja atualizar a pontuação de alguma equipe? (s/n): ")
    if opcao.upper() == 'S':
        id_equipe = int(input("Digite o ID da equipe que deseja atualizar a pontuação: "))
        nova_pontuacao = int(input("Digite a nova pontuação da equipe: "))
        cursor.execute("""UPDATE equipes SET pontuacao = ? WHERE id = ?""", (nova_pontuacao, id_equipe))
        conexao.commit()
        print(f"Pontuação da equipe com ID {id_equipe} atualizada para {nova_pontuacao}.")
    elif opcao.upper() == 'N':
        break
    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")

# processo de exclusão de equipes
while True:
    opcao = input("Deseja excluir alguma equipe? (s/n): ")
    if opcao.upper() == 'S':
        id_equipe = int(input("Digite o ID da equipe que deseja excluir: "))
        cursor.execute("""DELETE FROM equipes WHERE id = ?""", (id_equipe,))
        conexao.commit()
        print(f"Equipe com ID {id_equipe} excluída do banco de dados.")
    elif opcao.upper() == 'N':
        break
    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
print("--- FIM DO PROCESSO DE ATUALIZAÇÃO/EXCLUSÃO ---")
print("lista atualizada de equipes no banco de dados:")
cursor.execute("""SELECT * FROM equipes""")
equipes = cursor.fetchall()
for linha in equipes:
    print(f"-- ID: {linha[0]} | Nome da equipe: {linha[1]} | Nome do líder: {linha[2]} | Ano de fundação: {linha[3]} | Quantidade de membros: {linha[4]} | Pontuação: {linha[5]}")
print("--- FIM do PROGRAMA ---")