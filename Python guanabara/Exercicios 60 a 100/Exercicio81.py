import os

os.system('clear')

cont = 0

lista = list()

while True :
    n = int(input("Digite um numero :"))
    
    lista.append(n)
    
    lista.sort(reverse = True)
    
    opcao = str(input('Deseja continuar [S/N]'))
    
    cont += 1
    
    if opcao.upper() == 'N':
        break
    
os.system('clear')
    
print(f'Foram digitados {cont} numeros')
print(lista)
if 5 in lista:
    print('O numero 5 esta contido na lista')
else : 
    print('O numero 5 nao esta contido na lista')