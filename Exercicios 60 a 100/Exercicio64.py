import os

n = 0
soma = 0
q = 0


os.system("clear")

while n != 999:
    
    n = int(input("Digite o numero que deseja :"))
    
    if n != 999:
        soma += n 
        q += 1
    else :
        os.system("clear")
        print("Programa finalizado")

print("Foram digitados {} numeros e a soma desses numeros é igual a :{}".format(q,soma))
    