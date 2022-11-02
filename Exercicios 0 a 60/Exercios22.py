nome = input("Digite seu nome :")
contagem_espaco = nome.find(" ")
nomeseparado = nome.split()
primeiro = nome[:contagem_espaco]

print("""Dados pessoais de       :{} 
cujo o nomem em minusculo é :{}
Que contem {} letras 
Onde o primeiro nome é {}
E o primeiro nome contem {}""".format(nome.upper(),nome.lower(),len("".join(nomeseparado)),primeiro,len(primeiro)))
      