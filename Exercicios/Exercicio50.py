import os


import os

os.system("clear")

soma = 0

contagem = 0

for c in range(0,6):
    if c <= 0:
        numero = int(input("Digite um numero :"))
    else :
        numero = int(input("Digite outro numero:"))
    
    if numero%2 == 0:
        soma += numero
        contagem += 1
    
print("Foram digitados {} numeros pares e a soma desses numeros é igual a :{}".format(contagem,soma))