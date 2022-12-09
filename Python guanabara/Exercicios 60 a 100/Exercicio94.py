import os

os.system('clear')

list_names = list()
dictionary = dict()
list_with_person = list()
person  = average = woman  = names_age_average = 0

while True:
    dictionary['Name'] = str(input('Type the name :'))
    sex  = str(input('Type your sex [M/W] :')).upper()
    if sex not in 'MW' :
        sex  = str(input('Your answer is wrong please choose [M/W]:')).upper()
        if sex not in 'MW':
            print('erro in program ,try again')
            exit()
    dictionary['Sex'] = sex
    dictionary['Age'] = int(input('Type your age :'))
    option = input('Whould you like to continue [Y/N]:')
    
    person += 1
    
    list_names.append(dictionary.copy())
    
    if option in 'Nn':
        break
    
print('=' * 40)
print(f'{person} names were registered ')

for c in list_names :
    average += c['Age']
print(f'The average age recorded was  {average/person} years')
for c in list_names :
    auxiliar  = c['Sex'] 
    if auxiliar in 'W' :
        woman += 1
print(f"Was recorded {woman} woman's ")

for c in list_names :
    if c['Age'] >= (average/person):
        list_with_person.append(c)
print('List of people who are older than average')
for c in list_with_person:
    print(c)
        
    




         