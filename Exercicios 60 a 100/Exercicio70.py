nomes = []

preços = []

total = 0 

maisde8mil =0

contador = barato_preco = 1

barato_nome = ""

print("------------------------------------------------------------------------")
print("                         Lojas leais                                    ")
print("------------------------------------------------------------------------")

while True :
    produto = str(input("Digite o noma do produto :"))
    preço_produto = float(input("Digite o preço do produto R$:"))
    continuar = input("Deseja continuar [s/n] ?").upper()
    
    total += preço_produto
    
    if contador == 1 :
        barato_nome = produto
        barato_preco = preço_produto
    else :
        if preço_produto < barato_preco :
            barato_nome = preço_produto
            barato_nome = produto

    
    if preço_produto > 1000:
        maisde8mil += 1
    
    if continuar == "S" :
        nomes.append(produto)
        preços.append(preço_produto)
        print("------------------------------------------------------------------------")
    else :
        nomes.append(produto)
        preços.append(preço_produto)
        print("------------------------------------------------------------------------")
        break
    
local = min(preços)
    
print(f"""Total da compra foi de R$:{total}
Temos {maisde8mil} produtos custando acima de R$1000 
O produto mais barato foi {barato_nome} que custou {barato_preco}""")
    
        
## nao testado ainda