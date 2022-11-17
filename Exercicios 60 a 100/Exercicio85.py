import os

os.system('clear')

numeros = [[], []]

for c in range(0,7):
    n = int(input('Digite o numero que deseja adicionar a lista :'))
    
    if n%2 == 0:
        numeros[0].append(n)
    else :
        numeros[1].append(n)

numeros[0].sort()
numeros[1].sort()

print(f'Os numeros pares digitados foram :{numeros[0]}')
print(f'Os numeros impares digitados foram :{numeros[1]}')