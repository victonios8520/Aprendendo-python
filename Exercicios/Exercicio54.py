import os

idade =[]

os.system("clear")

for c in range (1,8):
    ano = int(input(f"Digite a data de nascimento a pessoa {c} :"))
    
    idade.append(ano)
    
    os.system("clear")

for c in range(0,7):
    print("Pessoa n°{} nacida em :{}".format(c+1,idade[c]) , end = " : ")
    if (2022-idade[c]) < 18 :
        print("Menor com :{} anos de vida!".format(2022-idade[c]))
    else:
        print("Maior com :{} anos de vida!".format(2022-idade[c]))
print("\n")