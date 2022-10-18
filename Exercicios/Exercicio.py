import math 
import random
import pygame



print("Exercicio 16\nExercicios17\nExercicio18\nExercicio19\nExercicio20\nExercicio21")

opcoes = int(input(":"))

if opcoes == 16 :
    numero = float(input("Digite um numero: "))
    numeroint = math.floor(numero)
    print("O numero digitado foi:{:.2f} a parte interira é {} ".format(numero ,int(numero)))
elif opcoes == 17:
    cateto = float(input("Qual o valor do cateto oposto: "))
    catetoadj = float(input("Qual o valor do cateto adjacente: "))

    #hipotenusa = math.sqrt(cateto**2 + catetoadj**2)

    hipotenusa = math.hypot(cateto ,catetoadj)

    print("O valor da hipotenusa é de {:.2f} ".format(hipotenusa))
elif opcoes == 18 :
    angulo = float(input("Digite o valor do angulo que voce deseja saber :"))
    sen = math.sin(math.radians(angulo))
    cos = math.cos(math.radians(angulo))
    tg = math.tan(math.radians(angulo))
    print("O agulo digitado foi de {:.2f} \nO seno desse angulo é de {:.4f}\nO coseno desse angulo é {:.4f}\nA tangente desse angulo é {:.4f}".format(angulo,sen ,cos,tg))
elif opcoes == 19:
    lista = []
    repeteco = 1
    while repeteco < 5 :
        nome = str(input("Digite o nome do {}° Aluno(a): ".format(repeteco)))
        lista.append(nome)
        repeteco += 1
    escolhido = random.choice(lista) 
    print("O aluno(a) escolhido foi:{}".format(escolhido))
elif opcoes == 20:
    lista = []
    repeteco = 1
    while repeteco < 5 :
        nome = str(input("Digite o nome do {}° Aluno(a): ".format(repeteco)))
        lista.append(nome)
        repeteco += 1
    escolhido = random.shuffle(lista) 
    print("A ordem de apresentação será:\n{}".format(lista))
elif opcoes == 21:
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load("tutu.mp3")
    pygame.mixer_music.play()
    pygame.event.wait()

else:
    print("Opção invalida")
