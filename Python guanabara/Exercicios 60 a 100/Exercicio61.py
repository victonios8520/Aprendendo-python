import os

os.system("clear")

primeiro = int(input("Digite o primeiro numero da sequancia :"))
razao = int(input("Digite a razao :"))
contador = 0

while contador < 10 :
    print("{} -> ".format(primeiro) ,end = "")
    primeiro = primeiro+razao
    contador += 1 
    