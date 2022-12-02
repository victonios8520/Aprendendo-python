import math

nota1 = int(input("Digite a primeira nota :"))

nota2 = int(input("Digite a segunda nota :"))

media = (nota1+nota2)/2

if media < 5 :
    print("Infelizmente voce nao passou de ano ")
elif 5 < media < 7:
    print("Recuperação")
else :
    print("Parabéns voce passou de ano")
