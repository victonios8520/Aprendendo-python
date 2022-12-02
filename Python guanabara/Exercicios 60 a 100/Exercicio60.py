import os

os.system("clear")

n = 1
opcao = int(input("Digite o numero que voce deseja saber o fatorial :"))
resultado = 1
if opcao >= 0 :
    print("O fatorial de é {}! = ".format(opcao) , end = "")
    while n <= opcao :    
        if n < opcao:
            print("{}".format(n),end = " X ")
        elif n == opcao :
            print("{}".format(n),end = " = ")
        resultado *= n
        n += 1
else:
    print("O numero digitado é invalido")
    

print(resultado)