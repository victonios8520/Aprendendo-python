print(12,30, sep = '_')

# se colocar \' ele iginora essa aspas no print
print('we aren\'t friends ')

a = 'Aaaa'
b = 'Bbbb'
c = 'Cccc'


string_1 = 'a={nome1}' 'b={nome2}' 'c={nome3}'
string = 'a={0}' 'b={1}' 'c={2}'

formato_1 = string.format(a , b ,c )
formato_2 = string.format(a , b , c)
formato_3 = string_1.format(
    nome1 = a 
    ,nome2 =b 
    ,nome3 = c
)


print(formato_1)
print(formato_2)
