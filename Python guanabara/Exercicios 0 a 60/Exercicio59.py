import time
import os

n = 0

while n != "N":
    os.system("clear")

    valor_1 = float(input("Digite o primeiro valor :"))
    valor_2 = float(input("Digite o segundo valor :"))
    opcao = 0
    
    while opcao != 4 :
        print("""Digite os numeros para as opcaoes abaixo 
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos numeros 
[5]Sair do programa""")
        opcao = int(input(":"))
        if opcao == 1 :
            print("{} + {} = {}".format(valor_1,valor_2,(valor_1+valor_2)))
        elif opcao == 2 :
            print("{} * {} = {}".format(valor_1,valor_2,(valor_1*valor_2)))
        elif opcao == 3:
            if valor_1 > valor_2 :
                print("O maior numero é {}".format(valor_1))
            else :
                print("O maior numero é {}".format(valor_2))
        elif opcao == 4 :
            for c in range(5,0,-1):
                print("Voce podera digitar novos numeros em {} segundos".format(c))
                time.sleep(1)
                os.system("clear")
        else :
            opcao = 4
            n = "N"
            os.system("clear")
            print("programa finalizado")
            
        time.sleep(2)
            
            
            
            
    
            
            