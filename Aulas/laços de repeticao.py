#conta de 6 a 2 cortando 2  exemplo: 6 4 2
for c in range(6,0,-2):
    print(c)
print("fim")

#conta de 6 a 0 exemplo :6 5 4 3 2 1 0
for c in range(6,0,-1):
    print(c)
print("fim")

# conta de 0 a 6
for c in range(0,6):
    print(c)
print("fim")

n = int(input("quantas vezes deseja repetir o laço "))
for c in range(0, n+1):
    print(c)

inicio = int(input("Digite o inicio:"))
fim = int(input("Digite o fim"))
passo = int(input("Digite o passo :"))

for c in range(inicio , fim+1 ,passo):
    print(c)