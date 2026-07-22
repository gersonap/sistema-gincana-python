# Este programa solicita ao usuário informações sobre uma equipe e exibe essas informações na tela.
nome_equipe = input("Digite o nome da equipe: ")
nome_lider = input("Digite o nome do líder da equipe: ")
ano_fundacao = input("Digite o ano de fundação da equipe: ")
qtde_membros = int(input("Digite a quantidade de membros da equipe: "))
pontuacao_inicial = 0

print("\nInformações da equipe cadastrada:")

# Exibe as informações fornecidas pelo usuário
print(f">> O nome da sua equipe é: {nome_equipe}")
print(f">> Nome do líder de sua equipe é: {nome_lider}")
print(f">> Ano de fundação da sua equipe é: {ano_fundacao}")
print(f">> Sua equipe tem {int(2026) - int(ano_fundacao)} anos de existência")
print(f">> A quantidade de membros da sua equipe é: {qtde_membros}")
pontuacao_inicial = qtde_membros * 50
print(f"A pontuação inicial da sua equipe é: {pontuacao_inicial}")
print("---fim---")

print("Cadastro realizado com sucesso!")
