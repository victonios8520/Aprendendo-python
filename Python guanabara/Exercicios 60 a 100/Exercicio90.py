aluno = dict()

aluno['Nome'] = input('Digite o nome do aluno :')
aluno['Media'] = input(f'Digite a media do(a) {aluno["Nome"]} :')

if int(aluno['Media']) < 5 :
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'

for k , n in aluno.items():
    print(f'{k} é igual a {n}')