from random import randint
import os
import time

jogador = dict()
maior = 0
contador = 0
os.system('clear')

for c in range(4):
    n = randint(1,6)
    print(f'Jogador {c+1} tirou ',n)
    jogador[f'Jogador {c+1}'] = n
    time.sleep(1)

print('\nGanhadores na ordem :\n')    
for k , v in sorted(jogador.items(),key=lambda item: item[1],reverse=True ):
    print(f'{k} Que tirou {v}')
    time.sleep(1)
            

            
    
        



    


    
        
    
    
    

    