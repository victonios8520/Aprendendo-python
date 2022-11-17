pessoas = list()
dado = list()
cont = maior = menor = 0

while True :
    dado.append(str(input('Digite o nome da pessoa que deseja cadastrar :')))
    dado.append(int(input('Digite o peso a pessoa :')))
    
    if cont == 0 :
        maior = dado[1]
        menor = dado[1]
    else : 
        if dado[1] >= maior :
            maior = dado[1]
        elif dado[1] <= menor :
            menor = dado[1]
        
    cont += 1
    pessoas.append(dado[:])
    dado.clear()
            
    if str(input('Deseja continuar ? :')).upper() == 'N' :
        break
    
print(f'Foram cadrastadas {cont} pessoas')    
print(f'O maior peso foi {maior}Kg ,peso de :',end = ' ')
for c in range(0,len(pessoas)):
    if pessoas[c][1] == maior :
        print(f'{pessoas[c][0]}',end = '')
print()
        
print(f'O maior peso foi {menor}Kg ,peso de :',end = ' ')
for c in range(0,len(pessoas)):
    if pessoas[c][1] == menor :
        print(f'{pessoas[c][0]}',end = ' ')
print()