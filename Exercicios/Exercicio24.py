nome = input("Digite o nome da cidade :")

nome_modificado = nome[:nome.find(" ")]

nome_modificado = nome_modificado.lower()

if  nome_modificado == "santo" :

    print("{} contem Santo no inicio do nome".format(nome.title()))
    
else :
    print("A cidade digitada nao contem a palavra 'santo' .")