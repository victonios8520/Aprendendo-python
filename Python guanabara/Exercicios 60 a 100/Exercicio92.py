import os
import datetime

data_hoje = datetime.date.today()

os.system('clear')

cadastro = dict()

cadastro['Nome'] = str(input('Digite o seu nome :')).title()
cadastro['Ano de nascimento'] = int(input('Digite o seu ano de nascimento :'))
cadastro['N° da carteira de trabalho'] = int(input('Digite o numero da sua carteira de trabalho (0 para nao tem ):'))

if cadastro['N° da carteira de trabalho'] != 0:
    cadastro['Ano de contratacao'] = int(input('Digite o ano de sua contratação :'))
    cadastro['Salario'] = int(input('Digite seu salario :'))
    aposentadoria  = 35 - (data_hoje.year - cadastro['Ano de contratacao'])
    if aposentadoria >= 0 :
        cadastro['Vai se Aposenta em'] = str(aposentadoria) + ' anos '
    else :
        cadastro['Aposentadoria'] = f'Voce ja deveria esta aposentado ha {aposentadoria*(-1)} anos atras '
 
print('=' *35)       
for k , v in cadastro.items():
    print(f'{k} : {v}')
print('=' *35) 

     
    
