numerais0 = ('ZERO','UM','DOIS','TRES','QUATRO','CINCO','SEIS','SETE','OITO','NOVE')
numerais1 = ('DEZ','ONZE','DOZE','TREZE','QUATROZE','QUINZE','DEZESEIS','DEZESETE','DEZOITO','DEZENOVE','VINTE')

while True:
    numero = int(input("Digite um numero de 0 a 20 :"))
    
    if 0 <= numero <= 20:
        break
    else:
        print(f"O numero {numero} nao esta entre 0 e 20 digite novamente:")
    
if numero < 10:
    print("Voce diditou o numero ",numerais0[numero])
else :
    print("Voce digitou o numero ",numerais1[numero-10])
