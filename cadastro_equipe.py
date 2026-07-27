class Equipe:
    def __init__(self, nome, lider, ano_fundacao, qtde_membros):
        self.nome = nome
        self.lider = lider
        self.ano_fundacao = int(ano_fundacao)
        self.qtde_membros = int(qtde_membros)
        self.idade = 2026 - self.ano_fundacao
        self.pontuacao_inicial = self.qtde_membros * 50

lista_equipes = []

while True:
    # Este programa solicita ao usuário informações sobre uma equipe e exibe essas informações na tela.
    nome_equipe = input("Digite o nome da equipe: ")
    nome_lider = input("Digite o nome do líder da equipe: ")
    ano_fundacao = input("Digite o ano de fundação da equipe: ")
    qtde_membros = int(input("Digite a quantidade de membros da equipe: "))
    nova_equipe = Equipe(nome_equipe, nome_lider, ano_fundacao, qtde_membros)
    lista_equipes.append(nova_equipe)
    print("\nInformações da equipe cadastrada:")

    # Exibe as informações fornecidas pelo usuário
    print(f"-- O nome da sua equipe é: {nome_equipe}")
    print(f"-- Nome do líder de sua equipe é: {nome_lider}")
    print(f"-- Ano de fundação da sua equipe é: {ano_fundacao}")
    print(f"-- Sua equipe tem {nova_equipe.idade} anos de existência")
    print(f"-- A quantidade de membros da sua equipe é: {qtde_membros}")
    print(f"-------: A pontuação inicial da sua equipe é: {nova_equipe.pontuacao_inicial}")
    print()
    continuar = input("Deseja cadastrar outra equipe? (s/n): ")
    if continuar.upper() == 'N':
        break
print("--- FIM DO PROCESSO DE CREDENCIAMENTO ---")
print("### Programa finalizado!")
print()
print()
print("Listagem das equipes cadastradas:")

for equipe in lista_equipes:
    print(f"\n-- Equipe: {equipe.nome} \n| Líder: {equipe.lider} \n| Ano de fundação: {equipe.ano_fundacao}\n| Idade: {equipe.idade} \n| Quantidade de membros: {equipe.qtde_membros} \n| Pontuação inicial: {equipe.pontuacao_inicial}\n")
