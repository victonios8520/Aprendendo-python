import os

os.system('clear')
palavras = ('apple','maca','tulio','vargem','viagem','eureka','lapis')
vogais = ('a','e','i','o','u')

print("="*60)
print("{:^60}".format("Letras"))
print("="*60)
for palavra in palavras :
    lista = ''
    for letras in palavra:
        for vogal in vogais:
            if letras == vogal:
                 lista += " " + vogal
    print('{:-<40} Temos:{}'.format(palavra.title(),lista))
    
