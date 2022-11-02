salario = float(input("Digite o valor de seu salario R$:"))

if salario <= 1250 :
    print("""O seu salario atual é de R$:{}
O aumento sera de R$:{}
O seu salario ficará R$:{}""".format(salario,(salario*0.15),salario+(salario*0.15)))
else :
    print("""O seu salario atual é de R$:{}
O aumento sera de R$:{}
O seu salario ficará R$:{}""".format(salario,(salario*0.1),salario+(salario*0.1)))