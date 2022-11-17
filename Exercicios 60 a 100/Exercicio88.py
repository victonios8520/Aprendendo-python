import random 
import time
import os

os.system('clear')

megasena = list()
jogos = list()
contador = 0

opcao = int(input('Digite quantos jogos deseja criar :'))

for c in range(0,opcao):
    while True:
        n = random.randint(1,60)
        if n not in jogos and contador < 6:
            jogos.append(n)
            contador += 1
        elif contador == 6 :
            contador = 0
            break
    jogos.sort()
    megasena.append(jogos[:])
    jogos.clear()
 
os.system('clear')
   
for c in range(0,opcao):
    print(megasena[c])
    time.sleep(2)
    