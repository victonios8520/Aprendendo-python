import os

os.system('clear')

names =  dict()
gols = list()
list_by_names = list()

while True:
    print('--'*30)
    names['Player'] = str(input('Type player name :'))
    
    goals_marck = int(input(f'How many games {names["Player"]} play ? :'))
    
    gols = list()
    
    total = 0
    
    for c in range(goals_marck):
        auxiliar = int(input(f'How many gols did {names["Player"]} score in the {c}° match: '))
        total += auxiliar
        gols.append(auxiliar)
        
    names['Goals'] = gols[:]
    names['Total'] = total
    
    list_by_names.append(names.copy())
        
    if  str(input('Do you wanna continue [Y|N]:')).upper() in 'N' :
        break
    

print('=+'*25)
print('{:<20} {:^20} {:^10}'.format('cod name','goals','total'))
for  e ,c in enumerate(list_by_names):
    print('{:^4}'.format(e) , end = '')
    print('{:<16} '.format(c['Player']) , end = '')
    print('{:^20}'.format(str(c['Goals'])), end = '')
    print('{:^10}'.format(c['Total']))
print('=+'*25)   
while True :
    option = int(input('Show the dada of which player (999 to exit) :'))
    
    if option != 999:
        if option < len(list_by_names):
            print(f'{list_by_names[option]["Player"]} dada survey')
            for e ,c in enumerate(list_by_names[option]['Goals']) :
                print(f'In game {e} scored {c} goals')
        else :
            print("This player doesn't exist")
    else :    
        break
print('Volte sempre')