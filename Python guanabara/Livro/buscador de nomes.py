import os

os.system("clear")

funcionarios = ["Victor Costa","Adriano Fontes","Andreia Gauval","Jorge Amaro","Joao Victor"]
telefone = [85203374,82647109,81647107,82537539,82745122]
nome = str(input("Digite o nome da pessoa que deseja buscar:").title())
quantos = 0
posicoes = []
telefone_lista = []
c = 0

for funcionarios in funcionarios:
    nome_int = funcionarios.find(nome)
    if nome_int >= 0:
        quantos += 1
        posicoes.append(funcionarios)
        telefone_lista.append(telefone[c])
    c += 1

if quantos > 1 :
    print("Achamos {} nomes".format(quantos))
    for c in range(0, quantos):
        print("[{}] {}".format( c ,posicoes[c]))
        
    print("""[0]Sair
Qual deles deseja escolher""")

    opcoes = int(input(":"))
    
    print("""Nome:{}
Telefone:{}""".format(posicoes[opcoes],telefone_lista[opcoes]))
    
else:
    print("""Nome:{}
Telefone:{}""".format(posicoes,telefone_lista))
    
        
        