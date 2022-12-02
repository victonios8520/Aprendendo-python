import time 
import os

os.system("clear")

lista_numeros = []
opcao = 0

for c in range(0,10):
    numero = int(input("Digite o N°{} da lista :".format(c+1)))
    lista_numeros.append(numero)
while opcao != 4 :
    print("""[1]Para saber o maior numero digitado
[2]Para saber o menor numero digitado
[3]O somatorio dos numeros
[4]Sair""")
    opcao  = int(input(":"))
    
    opcao  = int(input(":"))
    if opcao == 1 :
        print(max(lista_numeros))
    elif opcao == 2:
        print(min(lista_numeros))
    elif opcao == 3 :
        print(sum(lista_numeros))
    