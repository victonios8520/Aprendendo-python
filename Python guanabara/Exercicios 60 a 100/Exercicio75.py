pares = ""

print('=' * 40)
n = (float(input("Digite um valor :")),
    float(input("Digite outro valor :")),
    float(input("Digite mais um valor :")),
    float(input("Digite o ultimo valor :")))

for c , e in enumerate(n):
    if n[c]%2 == 0:
        pares += "{} ".format(int(n[c])) 
        
print('=' * 40)
print(f'Os numeros digitados foram {n}')
print(f'Foram digitador {n.count(9)} numeros 9')
if 3 in n :
    print(f'O primeiro 3 foi digitado na posicao {n.index(3)}')
else :
    print("Nao foi digitado nenhum numero 3")
print(f'Os numeros pares São {pares}')
print('=' * 40)