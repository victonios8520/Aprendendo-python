import os
import time

os.system('clear')

lista = list()

for j in range(3):
        coluna = list()
        for c in range(3):
            coluna.append(0) 
        lista.append(coluna[:])

while True:
           
    for j in range(3):
        for c in range(3):
            print(lista[j][c], end = ' ')
        print()
        
    time.sleep(0.2)
    os.system('clear')
    for c in range(3):
        lista[c][0] = 1
        
    for j in range(3):
        for c in range(3):
            print(lista[j][c], end = ' ')
        print()
        
    time.sleep(0.2)
    os.system('clear')
    for c in range(3):
        lista[c][1] = 1
        lista[c][0] = 0
        
    for j in range(3):
        for c in range(3):
            print(lista[j][c], end = ' ')
        print()
        
    time.sleep(0.2)
    os.system('clear')
    for c in range(3):
        lista[c][2] = 1
        lista[c][1] = 0
        
    for j in range(3):
        for c in range(3):
            print(lista[j][c], end = ' ')
        print()
        
    time.sleep(0.2)
    os.system('clear')
    
    for c in range(3):
        lista[c][2] = 0
        lista[c][1] = 0



        
    

