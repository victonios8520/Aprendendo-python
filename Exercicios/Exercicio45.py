import random
import time
import os 

print("###JokenPô###\n")

vezes = int(input("Eai vamos jogar de quantas partidas ? :"))

player1  = int(0)
player2  = int(0)

objetos = ["pe","pa","te"]


while player1 or player2 < vezes :
    escolha_pc = random.choice(objetos)
    
    escolha_player = str(input("""Digite oque vocer vai jogar :
pe para pedra
pa para papel 
te para tesoura
:"""))
    os.system("clear")
    print("player jogou :{} e o pc jogou :{}".format(escolha_player,escolha_pc))
    
    if escolha_player == escolha_pc :
        print("EMPATE!")
    elif escolha_player == "pe" and escolha_pc == "te" :
        print("Ponto para player :")
        print("ponto dos jogadores :")
        player1 = player1 +1
        print("pc com :{}".format(player1))
        print("jogador com :{}".format(player2))
    elif escolha_player == "pe" and escolha_pc == "pa" :
        print("Ponto para pc :")
        print("ponto dos jogadores :")
        player2 = player2 +1 
        print("pc com :{}".format(player1))
        print("jogador com :{}".format(player2))
    elif escolha_player == "te" and escolha_pc == "pa" :
        print("Ponto para player :")
        print("ponto dos jogadores :")
        player1 = player1 +1
        print("pc com :{}".format(player1))
        print("jogador com :{}".format(player2))
    elif escolha_player == "pa" and escolha_pc == "pe" :
        print("Ponto para player :")
        print("ponto dos jogadores :")
        player1 = player1 +1
        print("pc com :{}".format(player1))
        print("jogador com :{}".format(player2))
    elif escolha_player == "te" and escolha_pc == "pe" :
        print("Ponto para pc :")
        print("ponto dos jogadores :")
        player2 = player2 +1 
        print("pc com :{}".format(player1))
        print("jogador com :{}".format(player2))    
    elif escolha_player== "pa" and escolha_pc == "te" :
        print("Ponto para pc :")
        print("ponto dos jogadores :")
        player2 = player2 +1 
        print("pc com :{}".format(player1))
        print("jogador com :{}".format(player2))
        
    continuar = input("continuar ?:[s]")
    
    if continuar == "s" :
        os.system("clear")
    else :
        exit()  
        
        
if player1 > player2 :
    print("O pc ganhou com:{}pontos ".format(player1))
else :
    print("O jogador ganhou com :{}pontos ".format(player2))

