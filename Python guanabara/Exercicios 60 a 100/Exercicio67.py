while True :
    numero = int(input("Quer ver a tabuada de qual numero :"))    
    if numero >= 0 :
        print("------------------------------------------------------------------")
        for c in range(0,11):
            print(f"{c} X {numero} = {c*numero}")
        print("------------------------------------------------------------------")
    else :
        break
    