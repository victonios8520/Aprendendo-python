def voto(old = 0):
    import datetime
    year = datetime.date.today()
    age = year.year - old
    if age < 16 :
        mensage = f'Com {age} anos :Não vota'
    elif 16 <= age < 18 or age > 65 :
        mensage = f'Com {age} o Voto é opcional'
    else :
        mensage = f'Com {age} o Voto é Obrigatorio'
    return mensage


age = int(input('Digite em que ano voce nasceu :'))
print(voto(age))