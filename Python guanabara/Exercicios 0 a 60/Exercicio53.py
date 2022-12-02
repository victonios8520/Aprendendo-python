import os

os.system("clear")

palavra = str(input("Digite a palavra :")).strip()

quantidade = len(palavra)

lista_trocada = ""
lista_original = ("".join(palavra.split()))

print(lista_original)

for c in range(quantidade-1,-1,-1):
    lista_trocada += palavra[c]


os.system("clear")

print("".join(lista_trocada.split()) , "e lista :", lista_original)

if "".join(lista_trocada.split())  == lista_original :
    print("A frase ({}) é um palíndromo".format(" ".join(palavra.split())))
else :
    print("A frase '{}' nao é um palíndromo".format(" ".join(palavra.split())))
    