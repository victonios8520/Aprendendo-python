import os

os.system("clear")

tabuada = int(input("Digite o numero que deseja obter a tabuada: "))
quantidade = int(input("Digite ate que numero que deseja que sua tabuada vá: "))

os.system("clear")
print("#################################")
print("            TABUADA              ")
print("#################################")
for c in range(1 ,quantidade+1):
    print("{} X {}  = {}".format(tabuada,c ,tabuada*c))

print("#################################")   
