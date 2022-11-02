somatorio = 0

quantidade = 0

for c in range(1,500):
    if c%2 == 1:
        if c%3 == 0 :
            somatorio += c
            quantidade += 1
            
print("a soma de todos os {} itens somados foi igual a {}".format(quantidade ,somatorio))