matriz = [[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input(f'Digite o valor que deseja adicionar na linha|coluna [{j}|{i}] :')))
        
print('+'*30)

for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]}] ',end = '')
    print()
        
    
        
    
