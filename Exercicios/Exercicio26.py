nome = input("Digite o nome :").lower().strip()

print("""A letra A aparece {} vezes
A primeira letra aparece na posição {}
A ultima letra A aparece na posição {}""".format(nome.count("a"),nome.find("a"),nome.rfind("a")))

