print("#### Emprestimo Banco do Brasil ###")

nome = input("Digite seu nome :")
salario = float(input("Digite seu salario :"))
valor_casa = float(input("Digite o valor da casa desejada :"))
ano = int(input("Digite em quantos anos deseja pagar a casa :"))

prestacao = valor_casa/(ano * 12)

valor_emprestimo = salario*3.6*ano

if prestacao < (salario*0.3) :
    print("""### Banco do Brasil ###
Situacao do cliente {}
As parcelas do imovel mensais ficaram R$:{}
Apartir das analises da conta O emprestimo no valor de {}
FOI APROVADO!!!""".format(nome ,prestacao ,valor_casa))

else :
    print("""### Banco do Brasil ###
Situacao do cliente {}
As parcelas do imovel mensais ficaram R$:{:.2f}
Apartir das analises da conta O emprestimo no valor de {}
FOI negado.""".format(nome ,prestacao ,valor_casa))
    
print("O valor total disponivel para emprestimo no periodo de {} anos é de R$:{}".format(ano,valor_emprestimo))