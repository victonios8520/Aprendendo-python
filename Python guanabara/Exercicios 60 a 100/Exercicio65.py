import os
from statistics import median

q = 0
numeros = []
n = 0
opcao = ""
maior = 0 
menor = 0

while opcao != "N" :
    n = int(input("Digite o seu numero :"))
    numeros.append(n)
    opcao = str(input("Deseja continuar ?[S/N}:"))
    print(opcao)
    os.system("clear")
    
    # alternativa maior e menor
    #q += 1
    #if q == 1 :
    #   maior == n 
    #else :
        #if maior < n :
        #    maior = n
        #elif menor > n :
        #   menor = n
    

print("A media de todos os numeros digitados é :{}".format(median(numeros)))
print("A quantidade de numeros digitados foi :{}".format(len(numeros)))
print("O maior valor digitado foi {}".format(max(numeros)))
print("O menor valor digitado foi {}".format(min(numeros)))