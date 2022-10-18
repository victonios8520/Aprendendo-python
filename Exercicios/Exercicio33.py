numero1  = int(input("Digite o primeiro numero :"))
numero2  = int(input("Digite o segundo numero :"))
numero3  = int(input("Digite o terceiro numero :"))

if numero1 > numero2 and numero1 > numero3:
    print("O numero :{} é o maior ".format(numero1))
elif numero2 > numero1 and numero2 > numero3:
    print("O numero :{} é o maior ".format(numero2))
elif numero3 > numero1  and numero3 > numero2:
    print("O numero :{} é o maior ".format(numero3))
else :
    print("erro no codigo")