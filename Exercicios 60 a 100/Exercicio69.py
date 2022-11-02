import os

sexos = []

idades = []

pessoas = 0

mais18 = homens = mulheres = 0

os.system("clear")

while True :
    while True :    
        try : 
            #os.system("clear")
            idade = int(input("Digite a idade :"))
            break
        except ValueError:
            #os.system("clear")
            print("idade invalida")
    while True :       
         
        sexo = str(input("Digite o sexo [m/f] :")).upper()
        
        if sexo == "M" or sexo == "F":
            #os.system("clear")
            break
        else : 
            #os.system("clear")
            
            print("Sexo invalida ,digite novamente [m/f]")
    
    continuar = input("Se deseja continuar precione enter , caso nao precione qualquer tecla ....")
        
    if continuar  == "":
        sexos.append(sexo)
        idades.append(idade)
    else :
        sexos.append(sexo)
        idades.append(idade)
        break
    
for c in range(0,len(idades)):
    if idades[c] >= 18 :
        mais18 += 1
    if sexos[c] == "M" :
        homens += 1
    if sexos[c] == "F" and idades[c] >= 20 :
        mulheres += 1
        
    
print(f"""------------------- FIM DO PROGRAMA --------------------
Total de pessoas com mais de 18 anos é {mais18}
AO todo temos {homens} homens cadastrados
E temos {mulheres} mulheres com mais de 20 anos """)
