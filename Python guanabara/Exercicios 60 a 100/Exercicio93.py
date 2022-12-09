import os

os.system('clear')
jogador = dict()
jogos = list()
total = 0

jogador['Nome'] = str(input('Digite o nome do jogador :'))

opcao = int(input(f'Quantos jogos {jogador["Nome"]} jogou :'))

for c in range(opcao):
    jogos_pontuacao = int(input(f'Quantos gols {jogador["Nome"]} fez no Jogo {c+1} :'))
    jogos.append(jogos_pontuacao)
    total += jogos_pontuacao
jogador['Gols'] = jogos
jogador['total'] = total

print('='*40)
for k ,v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('='*40)

print(f'O jogador {jogador["Nome"]} jogou {opcao} partidas')

for c in range(opcao):
    print(f'Na partida {c+1} , fez {jogador["Gols"][c]} gols')
print(f'Foi um total de {jogador["total"]} gols')

