t0 = 1
t1 = 1
t2 = 0
repeticoes = 0

numero = int(input("Digite a quantidade de termos :"))

while repeticoes < numero :
    if repeticoes < 2:
        print(" {} ".format(t0) ,end = "->")
    else :
        print(" {} ".format((t0+t1)) ,end = "->")
        t2 = t1
        t1 = t0+t1 
        t0 = t2
    repeticoes += 1
print("Acabou")
    