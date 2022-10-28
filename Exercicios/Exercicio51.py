import os
os.system("clear")

fistone = int(input("Digite o primeiro termo da PA:"))

razao = float(input("Digite a razao:"))

os.system("clear")

print("OS 10 primeiros termos")


for c in range(2,12):
    print('{}'.format(fistone) , end = " -> ") 
    a = float(fistone +(c-(c-1))*razao)
    fistone = a
print("Acabou")