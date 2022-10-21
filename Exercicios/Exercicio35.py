primeiro = float(input("Digite o valor do primeiro segmento de reta :"))
segundo = float(input("Digite o valor do segundo segmento de reta :"))
terceiro = float(input("Digite o valor do terceiro segmento de reta :"))

if primeiro + segundo > terceiro :
    if segundo + terceiro > primeiro:
        if terceiro + primeiro > segundo:
            print("É possivel formar um triangulo !")
else:
    print("Não é possivel formar um tringulo")
