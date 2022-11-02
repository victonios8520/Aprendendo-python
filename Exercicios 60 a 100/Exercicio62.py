import os

os.system("clear")

primeiro = int(input("Digite o primeiro numero da sequancia :"))
razao = int(input("Digite a razao :"))
contador = 0
fechador  = 10

while contador <= fechador :
    if contador != fechador :
        print("{} ".format(primeiro) ,end = " -> ")
        primeiro = primeiro+razao
        contador += 1
    else :
        print("Lista")
        opcao = int(input("\nSe desejar continuar digite o numero de vezes a mais ,se nao digite 0:"))
        if opcao != 0:
            fechador += opcao
            contador = 0
            primeiro = 0
            os.system("clear")
        else : 
            os.system("clear")
            print("Processo finalizado")
            contador += fechador

        
        