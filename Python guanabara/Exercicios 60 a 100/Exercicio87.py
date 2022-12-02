matriz = [[],[],[]]
soma = soma_coluna = maior =0

for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input(f'Digite o valor que deseja adicionar na linha|coluna [{j}|{i}] :')))
        
print('+'*30)

for i in range(0,3):
    for j in range(0,3):
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        if j == 2 :
            soma_coluna += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]
        print(f'[{matriz[i][j]}] ',end = '')
    print()
    
print('+'*30)
    
print(f'A soma de todos os valores pares é igual a {soma}')
print(f'A soma de todos os valores da terceira coluna é : {soma_coluna}')
print(f'O maior valor da segunda linha é {maior}')