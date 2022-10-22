primeiro = float(input("Digite o valor do primeiro segmento de reta :"))
segundo = float(input("Digite o valor do segundo segmento de reta :"))
terceiro = float(input("Digite o valor do terceiro segmento de reta :"))

if primeiro + segundo > terceiro :
    if segundo + terceiro > primeiro:
        if terceiro + primeiro > segundo:
            if primeiro == segundo == terceiro :
                print("É possivel formar um triagulo Equilátero")
            elif primeiro == segundo or primeiro == terceiro or terceiro == segundo :
                print("É possivel formar um tringulo isóseles ")
            else:
                print("É possivel formar um triangulo Escaleno")
else:
    print("Não é possivel formar um tringulo")