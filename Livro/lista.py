um = [1,2,3]
dos = [4,5,6]
tre = [7,8,9]

lista = [um,dos,tre]

print(lista)

#adiciona o dos na posicao que voce quiase ,o de baixo add na posicao zero
lista.insert(0,dos)

print(lista)
#deleta oque ta na posicao 3
#o metodo pop
del(lista[3]) 
print(lista)

#remove o ultimo valor da lista
lista.pop()
print(lista)
#remove ele remove a variavel dentro da lista
lista = [um,dos,tre]
lista.remove(um)
print(lista)

valor = list(range(4,11))
print(valor)

desordenado = [0,4,6,3,2,8,5,7]
#o comando sort ele ordena a lista de forma crecente
print("Ordenado")
desordenado.sort()
print(desordenado)
#ordenado reverso
print("Desordenado reverto")
desordenado.sort(reverse=True)
print(desordenado)

a = [1,2,3,4]
# o b é igual ao a e esta ligado ao a se eu modificar b eu modifico A 
b = a
# ja esse de baixo significa que b recebe todos os indices de A ou seja uma copia
b = a[:]
