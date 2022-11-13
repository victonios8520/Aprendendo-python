lista_numeros = list()
a = 0

for i in range(0,5):
    n = int(input('Digite o numero :'))
    
    if i == 0  :
        print("O primeiro numero foi adicionado na lista")
        lista_numeros.append(n)
    elif n > max(lista_numeros):
        print("O numero foi adicionado no final da lista")
        lista_numeros.append(n)
    else :
        for p ,j in enumerate(lista_numeros):
            if n < min(lista_numeros) and j == min(lista_numeros):
                print('Foi adicionado no inicio da lista')
                lista_numeros.insert(p,n)
                break
            elif min(lista_numeros) < n < max(lista_numeros) and n <= j:
                print(f"Foi adicionada na posicao {p}")
                lista_numeros.insert(p,n)
                break
            elif min(lista_numeros) < n < max(lista_numeros) and n > j:
                print(f"Foi adicionada na posicao {p}")
                lista_numeros.insert(p+1,n)
                break
                
for p ,j in enumerate(lista_numeros):
    print(n , j)
print(lista_numeros)