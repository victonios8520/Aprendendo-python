def fatorial(a = 1,b = False):
    f = 1
    for c in range(a , 0 , -1 ):
        if b == True:
            f *= c
            if c > 1 :
                print(f'{c}', end = ' X ')
            else:
                print(c ,end = ' = ')
        else :
            f *= c
    return f
    
    
nun = int(input('Digite o valor do fatorial desejado:'))
opcao = str(input('Digite S caso queira mostar a resolucao :'))
if opcao in 'Ss':
    opcao = True
print(fatorial(nun,opcao))

