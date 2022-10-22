peso = float(input("Digite o peso em Kg:"))
altura = float(input("Digite a sua altura em metros:"))

       
imc = peso /(altura**2)

if imc <= 18.5 :
    print("Voce esta abaixo do peso")
elif  18.5 < imc <= 25 :
    print("Seu peso é ideal")
elif 25 < imc <= 30 :
    print("Voce esta sobre peso ")
else :
    print("Obsidade morbida")
    
    