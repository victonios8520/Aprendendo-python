nome = str(input("Digite seu nome :")).lower().strip()



print(""" O seu nome completo é {}
O primeiro nome é :{}
O ultimo nome é :{}""".format(nome.title(),nome[:nome.find(" ")].title(),nome[nome.rfind(" "):].title().strip()))

# outra possibilidade 

print("\n\n\n")

n = nome.split()

print("Seu primeiro nome é {}".format(n[0]))

print("Seu ultimo nome é ",n[len(n)-1].title())
