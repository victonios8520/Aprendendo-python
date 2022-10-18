#velocidade do carro
import playsound

quantidade = int(input("Digite a quantidade de repeticoes :"))

repeticoes = 0 + 1 

while repeticoes < quantidade + 1:
    print("Simulacao {}".format(repeticoes))
    leitor = float(input("Digite a velocidade do carro :"))
    if leitor > 80 :
        print("MUlTADO!")
        playsound.playsound("audio.mp3")
        multa = (leitor - 80)*7
        print("O valor da multa ficou R$:{:.2f}\n".format(multa))
    else :
        print()
        
    repeticoes += 1
    

    