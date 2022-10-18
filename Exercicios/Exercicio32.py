ano = int(input("Digite o ano  :"))

bissexto = ano % 4

if bissexto == 0 :
    print("Esse é um ano bissexto ")
else:
    print("Esse ano nao é bissexto")