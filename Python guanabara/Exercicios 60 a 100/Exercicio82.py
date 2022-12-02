import os

os.system('clear')

par = list()
impar = list()
numeros = list()

while True :
    n = int(input('Digite um numero:'))
    opcao = str(input('Deseja continuar ? [S/N] :'))
    numeros.append(n)
    if opcao.upper() == 'N':
        break
for c in numeros:
    if c%2 == 0:
        par.append(c)
    else :
        impar.append(c)

print(f'A lista digitada foi :{numeros}')
print(f'A lista par é : {par}')
print(f'A lista impar é : {impar}')
