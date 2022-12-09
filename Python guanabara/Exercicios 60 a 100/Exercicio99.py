def maior(*a):
    maior = 0
    print('Analizando dados ...')
    print(f'{a} Foram imformados {len(a)} valores ao todo .')
    for c in a :
        if maior < c:
            maior = c
    print(f'O maior entre eles {maior}')


maior(1000,20,300,90,50,301,70,80)
maior(10,20,300,100,80)
maior(10,20,200)
maior(10,20)
maior(10,20,380)
maior(10)
            