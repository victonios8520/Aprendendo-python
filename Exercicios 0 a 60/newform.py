#this biblioteca use an audio mp3 ,thisis the best biblioteca

import playsound

nome = str(input("Digite o nome da musica seguido de mp3 :"))
playsound.playsound("{}.mp3".format(nome))

nome_1 = input ("Digite qualquer coisa")

print("uau voce digitou : {}".format(nome_1))