nome = input("Digite seu nome :")
#conta quantos caracteres tem em umaq frase
contador   = len(nome)
#conta quantas vezes tem uma letre na frase 
contador_letra = nome.count(" ")
#contador mais o fateador
contador_letra_fatiador = nome.count(" ",0,13)
#informa onde ele encontrou uma determinada frase
contador_frase = nome.find(" ")
# retorna um true ou false para uma frase 
Boleano  = "Victor" in nome 
#mostra o primeiro Nome
print("Seu primeirop nome é :",nome[:contador_frase])
contador  = 30
#Substituicao de frase de uma por outra,ele substitui em outra str
nome_mood = nome.replace("Victor","Maria")
#upper fica tudo em maiusculo
maiusculo = nome.upper()
#lower fica tudo minusculo
minusculo = nome.lower()
#capitalize trasforma somente a primeira letra em maiusculo e o ressto em minusculo
primeira = nome.capitalize()
#tittle vai fazer uma analise e trasforma cada letra da palavra em maiusculo
maiusculo_primeira = nome.title()
#strip remove os espacos inuteis tanto no inicio quanto no final
inultil = nome.strip()
#rstrip so apaga os espaços a direita
#lstrip so apaga os espaços a esquerda
#split divide em frases os espaços
lista = nome.split()
#join junta varios caracteres
uniao = "_".join(lista)
print(contador_letra)
print(contador_letra_fatiador)
print(contador_frase)
print(Boleano)
print(nome_mood)
print(maiusculo)
print(minusculo)
print(primeira)
print(maiusculo_primeira)
print(inultil)
print(lista)
print(uniao)




