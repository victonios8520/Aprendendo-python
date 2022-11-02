import os 

os.system("clear")

maior_idade = 0
nome_maior = ""
media = 0
quantidade = 0

for c in range(0,4):
    nome = str(input("Digite o nome da pessoa n°{} :".format(c+1)))
    sexo = str(input("Digite o sexo :[M|F] :").lower())
    idade = int(input("Digite a sua idade :"))
    print("\n")
    
    print(sexo)
    
    media = media+idade
       
    
    if sexo == "m" :
        if idade > maior_idade :
            maior_idade = idade
            nome_maior = nome
        elif idade == maior_idade:
            nome_maior = " ('Existe 2 ou mais pessoas com idades iguais')"
    else :
        if idade < 20 :
            quantidade = quantidade + 1
            

print("""A media de idade do grupo é :{} .
O homem mais velho é o :{}.
Existem {} mulheres com menos de 20 anos .""".format((media/4),nome_maior.title(),quantidade))