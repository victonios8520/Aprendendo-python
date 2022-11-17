import os 

os.system('clear')

experssao = str(input('Digite a expressao que voce deseja analisar:'))

parenteses_d = parenteses_e = 0

for c in experssao:
    if c == '(':
        parenteses_d += 1
    elif c == ')':
        parenteses_e += 1

if parenteses_e == parenteses_d:
    print("A expressao esta correta !")
else :
    print("A expressao esta errada !")