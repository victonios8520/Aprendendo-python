from imp import acquire_lock
import os

os.system("clear")

lista = []

maior  = 0


for c in range(0,5):
    peso = float(input("Digite o pesso da pessoa n°{} :".format(c+1)))
    lista.append(peso)
    menor = peso
    
for c in range(0,5):
    for m in range(0,5):
        if lista[c] > lista[m] and  lista[c] > maior:
            maior = lista[c]
        if lista[c] == lista[m]:
            print()
        if lista[c] < lista[m] and lista[c] < menor :
            menor  = lista[c]
            
print("""O MAIOR PESO DA LISTA É :{}
O MENOR PESO DA LISTA É :{} """.format(maior, menor))