preço = float(input("Digite o valor do produto :"))

forma = int(input("""Digite a opçao :
1_A vista dinheiro 
2_A vista Cartao 
3_a Prazo Cartão
:"""))

if forma == 1:
    valor = preço - (preço*0.1)
    print("O valor do produto será de R${:.2f}".format(valor))
elif forma == 2:
    valor = preço - (preço*0.05)
    print("O valor do produto  será de R${:.2f}".format(valor))
elif forma == 3 :
    forma = int(input("Será dividido em quantas vezes :"))
    if forma <= 2 :
        print("O valor do produto sera de R${:.2f} e as parcelas ficaram de R${:.2f} por mes".format(preço,(preço/2)))
    else :
        print("o valor do produto será de R${:.2f} e as parcelas sairam por R${:.2f}".format((preço+(preço*0.2)),(preço+(preço*0.2))/forma))
    
