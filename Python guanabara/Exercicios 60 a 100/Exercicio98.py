import time
import os

os.system('clear')

def contagem(a , b , c):
    print('+='*20)
    contador = a
    if c < 0 :
        c = c*-1
    if a < b:
        print(f'Fazendo a contagem de {a} ate {b} de {c} em {c} :')
        while contador <= b :
            print(f'{contador}' , end = ' ')
            contador += c
            time.sleep(0.2)
    else :
        print(f'Fazendo a contagem de {a} ate {b} de {c} em {c} :')
        while contador >= b :
            print(f'{contador}' , end = ' ')
            contador -= c
            time.sleep(0.2)
        
    print()
    
        
contagem(1,10,1)

contagem(10,0,2)

print('+='*20)
print('Agora e sua hora de personalizar :')

inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo :'))

contagem(inicio,fim,passo)