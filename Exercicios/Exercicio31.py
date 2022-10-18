distancia = int(input("Digite a distancia percorrida em km:"))

if distancia <= 200 :
    print("O valor da viajem será de R$:{:.2f}".format(distancia*0.5))
else :
    print("O valor da viajem será de R$:{:.2f}".format(distancia*0.45))