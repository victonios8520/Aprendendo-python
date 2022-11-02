nome = input("Digite o seu nome :")

boloano = "silva" in nome.lower()

if boloano == True :
    print("{} contem Silva no nome".format(nome.title()))
    
else :
    print("{} nao contem 'Silva' .".format(nome.title()))