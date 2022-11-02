import random

vitorias = 0

while True :
    numero = int(input("Digite o seu numero :"))
    
    pc = int(random.randint(0,10))
    
    resultado = (pc+numero)%2
    
    parouimpar = input("Par ou impar [P/I] :")
    
    if parouimpar == "p" or parouimpar == "p" :
        if resultado == 0 :
            print(f"Voce jogou {numero} e o computador {pc} o total de {(pc+numero)} PAR")
            print("voce ganhou !!!")
            vitorias += 1
        else :
            print(f"Voce jogou {numero} e o computador {pc} o total de {(pc+numero)} IMPAR")
            print("Voce perdeu!")
            break
    elif parouimpar == "I" or parouimpar == "i":
        if resultado == 1 :
            print(f"Voce jogou {numero} e o computador {pc} o total de {(pc+numero)} IMPAR")
            print("voce ganhou !!!")
            vitorias += 1
        else :
            print(f"Voce jogou {numero} e o computador {pc} o total de {(pc+numero)} PAR")
            print("Voce perdeu!")
            break
print(f"Voce venceu o computador {vitorias} vezes.")
        
    