soma = 0
quantidade = 0

while True :
    n = int(input("Digite um valor ou 999 para parar :"))
    if n == 999:
        break
    quantidade += 1
    soma += n
    
print(f"A soma dos {quantidade} valores é {soma}")
