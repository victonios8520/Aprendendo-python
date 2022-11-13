lista = list()
posicao_m = list()
posicao_n = list()

for c in range(0,5):
    lista.append(input(f"Digite o {c+1}° numero :"))
    
print(f"A lista digitada foi {lista}")
print(f"O maior valor é igual a {max(lista)} e esta localizado nas posicoes :",end ="")       
for p ,l in enumerate(lista) :
    if l == max(lista):
        print(f'{p} ',end ='')      
print(f"\nO menor valor é igual a {min(lista)} e esta localizado nas posicoes :",end="")


for p ,l in enumerate(lista) :
    if l == min(lista):
        print(f'{p} ',end ='')
print()
           