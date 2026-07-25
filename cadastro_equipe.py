# Definindo funções do programa
def calcular_pontuacao(qtde_membros):
    pontos = qtde_membros * 50
    return pontos

def verificar_qualificacao(qtde_membros): 
    if qtde_membros >= 10:
        return print("STATUS: Equipe Qualificada!!!!")
    else:
        return print("STATUS: Equipe NÃO Qualificada!!!!")

def calcular_idade(ano_fundacao):
    idade = 2026 - int(ano_fundacao)
    return idade

lista_equipes = []
while True:
     # Este programa solicita ao usuário informações sobre uma equipe e exibe essas informações na tela.
    nome_equipe = input("Digite o nome da equipe: ")
    nome_lider = input("Digite o nome do líder da equipe: ")
    ano_fundacao = input("Digite o ano de fundação da equipe: ")
    qtde_membros = int(input("Digite a quantidade de membros da equipe: "))
    pontuacao_inicial = 0

    print("\nInformações da equipe cadastrada:")

    # Exibe as informações fornecidas pelo usuário
    print(f"-- O nome da sua equipe é: {nome_equipe}")
    print(f"-- Nome do líder de sua equipe é: {nome_lider}")
    print(f"-- Ano de fundação da sua equipe é: {ano_fundacao}")
    print(f"-- Sua equipe tem {calcular_idade(ano_fundacao)} anos de existência")
    # print(f"-- Sua equipe tem {int(2026) - int(ano_fundacao)} anos de existência")
    print(f"-- A quantidade de membros da sua equipe é: {qtde_membros}")
    pontuacao_inicial = calcular_pontuacao(qtde_membros)
    print(f"-------: A pontuação inicial da sua equipe é: {pontuacao_inicial}")
    verificar_qualificacao(qtde_membros)
    print(" ")
    # print("Cadastro realizado com sucesso!")
    print(" ")
    dados_equipe = {"nome": nome_equipe, 
                    "lider": nome_lider,
                    "ano": ano_fundacao,
                    "idade": calcular_idade(ano_fundacao), 
                    "membros": qtde_membros, 
                    "pontuacao": pontuacao_inicial}
    lista_equipes.append(dados_equipe)
    continuar = input("Deseja cadastrar outra equipe? (s/n): ")
    if continuar.upper() == 'N':
        break
print("--- FIM DO PROCESSO DE CREDENCIAMENTO ---")
print("### Programa finalizado!")
print(" ")
print(" ")
print("Listagem das equipes cadastradas:")
for equipe in lista_equipes:
    print(f"\n-- Equipe: {equipe['nome']} \n| Líder: {equipe['lider']} \n| Ano de fundação: {equipe['ano']}\n| Idade: {equipe['idade']} \n| Quantidade de membros: {equipe['membros']} \n| Pontuação inicial: {equipe['pontuacao']}\n")
#print(f"Equipes cadastradas: {', '.join(lista_equipes)}")