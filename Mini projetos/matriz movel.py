from random import randint

lista = list()
verificador = 0
pessoas = infectados = morto = 0

for i in range(0,10):
    coluna = list()
    for j in range(0,10):
        n = randint(0,3)
        if n is not coluna and verificador <= 10:
            coluna.append(n)
    lista.append(coluna[:])

print(lista,'\n\n')
print('_'*41)
for i in range(0,10):
    coluna = list()
    print('|',end = '')
    for j in range(0,10):
        print('{:^3}'.format(lista[i][j]) ,end = '|')
        if lista[i][j] == 0 :
            morto += 1
        elif lista[i][j] == 1 :
            pessoas += 1
        elif lista[i][j] == 2 :
            infectados += 1
    print()
    print('-'*41)

    
print('''Existem na tabela {} pessoas saudaveis 
Existem {} pessoas infectadas
Existem {} mortos '''.format(pessoas,infectados,morto))

while True:
    opcao = input('Digite qual das pessoas deseja saber o estado:').strip().split()
    print(lista[int(opcao[0])][int(opcao[1])])
    
    if opcao != 999 :
        opcao = input('Digite qual das pessoas deseja saber o estado:').strip().split()
        print(lista[int(opcao[0])][int(opcao[1])])
    else :    
        break

