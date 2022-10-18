from random import randint
import emoji 

print("Joguinho do adivinha")

numero = int(input("Digite aqui seu palpite :"))

pc = randint(0,5)

if numero == pc :
    print(emoji.emojize("Parabéns voce acertou ! 😎"))
else :
    print(emoji.emojize("Sinto muito mas voce errou 🙁 "))
    print("O numero correto era :",pc)