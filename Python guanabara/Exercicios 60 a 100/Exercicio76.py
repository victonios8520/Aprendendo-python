import os
os.system('clear')

lista = ('Pao',1.50,'Leite',7.00,'Gurana',8.00,'Maça',3.00,'Coca cola',6.00)

print("_"*60)
print("|{:^58}|".format("Listagem de preços"))
print("_"*60)

for c in range(0,len(lista),2):
    print('|{:.<50}'.format(lista[c]),end = 'R$:')
    print('{:>5}|'.format(lista[c+1]))
print("_"*60)