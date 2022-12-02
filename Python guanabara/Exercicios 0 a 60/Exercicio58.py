import random 
import os
import time

os.system("clear")

n = -1
quantidade = 0
palavra = "PARABENS!!"

numero = random.randrange(11)

while n != numero :
    player = int(input("Digite seu palpite entre 0 a 10 :"))
    if player  == numero :
        n = numero
        quantidade += 1
        os.system("clear")
        for m in range(0,5): 
            for c in range(0,10):
                if c < 9 :
                    print(palavra[c] ,end = "")
                    time.sleep(0.15)
                else :
                    os.system("clear")
                    
    else :
        quantidade += 1
        print("Errado !")
        time.sleep(0.5)
        os.system("clear")
        
print("Parabens voce acertou em {} tentativas ".format(quantidade))