import os

os.system("clear")

palavra = str(input("Digite a palavra :"))

quantidade = len(palavra)

lista = ""

for c in range(quantidade-1,-1,-1):
    if palavra[c] != " " :
        print("ola dinovo")
        print(palavra[c])
        


##os.system("clear")
print(lista)
if lista == palavra :
    print(f"A frase ({lista}) é um palíndromo")
else :
    print(f"A frase ({lista}) nao é um palíndromo")
    
    
    #programa em fase de confecxao e o exercico 51 nao foi feito ainda