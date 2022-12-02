import os

os.system('clear')

print('=' * 30)
print(':^30'.format("BANCO DA CIDADE"))
print('=' * 30)
cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0

dinheiro = float(input('Digite o valor que deseja sacar :'))

while True :
    if dinheiro/50 >= 1:
        cedulas50 = int(dinheiro/50)
        dinheiro = dinheiro - (int(dinheiro/50))*50
        
    if dinheiro/20 >= 1:
        cedulas20 = int(dinheiro/20)
        dinheiro = dinheiro - (int(dinheiro/20))*20
        
    if dinheiro/10 >= 1:
        cedulas10 = int(dinheiro/10)
        dinheiro = dinheiro - (int(dinheiro/10)*10)
        
    if dinheiro/1 >= 1:
        cedulas1 = int(dinheiro/1)
        dinheiro = dinheiro - int(dinheiro/1)
        
    if dinheiro == 0 :
        break
    
print("Total de {} de cedulas de R$50,00     ".format(cedulas50))
print("Total de {} de cedulas de R$20,00     ".format(cedulas20))
print("Total de {} de cedulas de R$10,00     ".format(cedulas10))
print("Total de {} de cedulas de R$1,00     ".format(cedulas1))
print('=' * 30)
    
    