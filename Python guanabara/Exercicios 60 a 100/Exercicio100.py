from random import randint

def sorteio(nun):
    nun_saida = list()
    print('Os numeros sorteados foram :',end = '')
    contador = 0
    while True :
        n = randint(0,len(nun)-1)
        if nun[n] not in nun_saida:
            nun_saida.append(nun[n])
            print(nun_saida[contador] , end = ' ')
            contador += 1
        if contador >= 5:
            print()
            break    
    nun.clear()
    for c in nun_saida:
        nun.append(c)
 
def soma(nun):
    print('Somando os valores pares de ' ,end = '')
    pares = 0
    for c in nun:
        print(c,end = ' ')
        if c % 2 == 0:
            pares += c
    print(f'temos {pares}')
           

numeros = [10,11,23,42,45,56,76,77,87,32,33,43,59,20,30,40,50,60,70,80,90]

sorteio(numeros)

soma(numeros)

