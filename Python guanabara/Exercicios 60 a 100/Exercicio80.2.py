import os 

lista_n = list()

os.system('clear')

for c in range(0,5):

    n= int(input('Digite o numero que deseja add a lista :'))
    if c == 0 :
        print("O primeiro numero foi adicionado na lista")
        lista_n.append(n)
    elif n > max(lista_n):
        lista_n.append(n)
        print(f'O numero {n} foi adicionado no fim da lista')
    elif n < min(lista_n):
        lista_n.insert(0,n)
        print(f'O numero {n} foi adicionado no incio da sua lista')
    else:
        for p , l_n in enumerate(lista_n):
            if n < l_n :
                lista_n.insert(p,n)
                print(f'O numero {n} foi adicionado na posicao {p}')
                break
print(lista_n)