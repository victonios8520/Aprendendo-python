numeros = list()

while True:
    numero = input('Digite um numero:')
    
    if numero in numeros :
        print('Esse numero ja foi adcionado na lista digite um valor diferente')
    else :
        print('Adicionado com sucesso')
        numeros.append(numero)
    
    opcao = input("Deseja continuar [s/n] :")
    
    if opcao.lower().strip() != 's':
        break
    
print(f"OS valores digitados foram {numeros}")