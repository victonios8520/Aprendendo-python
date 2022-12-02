import os

n = 0 

os.system("clear")

while n < 1:
    sexo = input("Digite o seu sexo : [M/F] :")
    
    if sexo == "M" or sexo == "F":
        n += 1
    else :
        print("Digite uma opcao valida [M/F] a opcao digitada {} nao é valida".format(sexo))
        
os.system("clear")