numero = int(input("Digite o numero que voce deseja :"))
opca0 = int(input("""Digite a opção desejada
1 - Binario 
2 - Octal
3- hexadecimal 
:"""))

numero_convertido = []

if opca0 == 1 :
    if numero <= 256 :
        if int(numero/128) >= 1 :
            numero = numero - 128
            numero_convertido.append("1")
        else :
            numero_convertido.append("0")
        if int(numero/64) >= 1 :
            numero = numero - 64
            numero_convertido.append("1")
        else :
            numero_convertido.append("0")
        if int(numero/32) >= 1 :
            numero = numero - 32
            numero_convertido.append("1")
        else :
            numero_convertido.append("0")
        if int(numero/16) >= 1 :
            numero = numero - 16
            numero_convertido.append("1")
        else :
            numero_convertido.append("0")
        if int(numero/8) >= 1 :
            numero = numero - 8
            numero_convertido.append("1")
        else :
            numero_convertido.append("0")
        if int(numero/4) >= 1 :
            numero = numero - 4
            numero_convertido.append("1")
        else :
            numero_convertido.append("0")
        if int(numero/2) >= 1 :
            numero = numero - 2
            numero_convertido.append("1")
        else :
            numero_convertido.append("0")
        if int(numero/1) >= 1 :
            numero = numero - 1
            numero_convertido.append("1")
        else :
            numero_convertido.append("0")
        
        numero_final = "".join(numero_convertido)
        
        print("Em binario o numero é :{}".format(numero_final))  
               
    else:
        print("Erro esse numero é maior que o possivel")
        
elif opca0 == 2 :
    if numero <= 4096:
        if int(numero/512) >= 1 :
            numero_convertido.append(int(numero/512))
            numero = numero - 512*(int(numero/512))
        else :
            numero_convertido.append(0)
        if int(numero/64) >= 1 :
            numero_convertido.append(int(numero/64))
            numero = numero - 64*(int(numero/64)) 
        else :
            numero_convertido.append(0)
        if int(numero/8) >= 1 :
            numero_convertido.append(int(numero/8))
            numero = numero - 8 * (int(numero/8))
        else :
            numero_convertido.append(0)
        if int(numero/1) >= 1 :
            numero_convertido.append(int(numero/1))
        else :
            numero_convertido.append(0)
              
        letra = (str(numero_convertido))
         
        print("Em binario o numero é :{}".format(''.join(map(str, numero_convertido))))
        
    else :
        print("Erro esse numero é maior que o possivel")
elif opca0 == 3:
    if numero <= 4096 :
        if int(numero/256) >= 1 :
            if int(numero/256) <= 9:
                letra = int(numero/256)
                numero_convertido.append(str(letra))
            elif int(numero/256) == 10 :
                numero_convertido.append("A")
            elif int(numero/256) == 11 :
                numero_convertido.append("B")
            elif int(numero/256) == 12 :
                numero_convertido.append("C")
            elif int(numero/256) == 13 :
                numero_convertido.append("D")
            elif int(numero/256) == 14 :
                numero_convertido.append("E")
            elif int(numero/256) == 15 :
                numero_convertido.append("F")
            numero = numero - 256*(int(numero/256))
        else :
            numero_convertido.append("0")
               
        if int(numero/16) >= 1 :
            if int(numero/16) >= 1 :
                if int(numero/16) <= 9:
                    letra = int(numero/16)
                    numero_convertido.append(str(letra))
                elif int(numero/16) == 10 :
                    numero_convertido.append("A")
                elif int(numero/16) == 11 :
                    numero_convertido.append("B")
                elif int(numero/16) == 12 :
                    numero_convertido.append("C")
                elif int(numero/16) == 13 :
                    numero_convertido.append("D")
                elif int(numero/16) == 14 :
                    numero_convertido.append("E")
                elif int(numero/16) == 15 :
                    numero_convertido.append("F")
            else :
                numero_convertido.append("0")
                
                numero = numero - 16*(int(numero/16))   
        if int(numero/1) >= 1 :
            if int(numero/1) >= 1 :
                if int(numero/1) <= 9:
                    letra = int(numero/1)
                    numero_convertido.append(str(letra))
                elif int(numero/1) == 10 :
                    numero_convertido.append("A")
                elif int(numero/1) == 11 :
                    numero_convertido.append("B")
                elif int(numero/1) == 12 :
                    numero_convertido.append("C")
                elif int(numero/1) == 13 :
                    numero_convertido.append("D")
                elif int(numero/1) == 14 :
                    numero_convertido.append("E")
                elif int(numero/1) == 15 :
                    numero_convertido.append("F")
        else :
            numero_convertido.append("0")
            
        print("Em binario o numero é :{}".format(''.join(numero_convertido)))

    else :
        print("Erro esse numero é maior que o possivel")
else :
    print("Opção invalida :")
    


    
        