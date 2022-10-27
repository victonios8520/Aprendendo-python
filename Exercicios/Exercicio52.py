import os 

os.system("clear")

numero = int(input("Digite o numero que voce deseja sabe se é primo :"))

contagem  = 0

for c in range(1,numero+1):
    if numero%c == 0 :
        contagem+=1
    
    
if contagem > 2 or numero ==1:
    print(f"O numero {numero} nao é um numero primo")
else :
    print(f"O numero {numero} é um numero primo")