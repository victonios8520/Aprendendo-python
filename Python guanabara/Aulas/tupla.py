tupla = ("Hamburge","Batata frita" ,"arroz" , "Batata" )
#mostra c = ao nome do item e p a numeracao do item
for c , p in enumerate(tupla):
    print("item {} and numerecao {}".format(p,c))
#para colocar a turpla em ordem 
print(sorted(tupla))

a = (1,2,3,4,5)
b = (6,7)
c = a+b
#quantas vezes o numero aparece dentro da tupla
print(c.count(2))    
#index é para saber qual a posicao do 8
print(c.index(3))
#pode conter dados diferentes na tupla 
dados = ("nome:gustavo",18,"m",1.90)
print(dados)
#deletar uma tupla
noems = ("victor","costa")
del(noems)
print(noems) #vai da erro