numero = 0
criterio = 0

for c in range(0,13):
    criterio = c-6
    if criterio < 0 :
        numero = (c-6)*(-1)
    else :
        numero = c-6
        
    print(numero)
    
