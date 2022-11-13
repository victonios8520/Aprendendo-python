l_numero = list()
ordenada = list()

for l in range(0,5):
    l_numero.append(int(input("Digite um numero :")))
    
for j in range(0,len(l_numero)):
    ordenada.append(min(l_numero))
    l_numero.remove(min(l_numero))
print(ordenada)
