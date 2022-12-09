def ficha(name = '<Desconhecido>', goals = 0):
    if gols.isnumeric() ==  False and name.strip() == '':
        name = '<Desconhecido>'
        goals = 0
    elif gols.isnumeric() == False:
        goals = 0
    elif name.strip() == '':
        name = '<Desconhecido>'
    retorno = f'O jogador {name} fez o total de {goals} gols'
    return retorno

nome = input('Digite o nome do jogador :')
gols = input('Digite a quantidade de gols :')

print(ficha(nome,gols))