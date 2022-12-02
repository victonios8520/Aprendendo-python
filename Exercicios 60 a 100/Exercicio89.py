import os

os.system('clear')

alunos = list()
contador = 0

while True :
    contador  += 1
    aluno = list()
    aluno.append(str(input(f'Digite o nome do {contador}° aluno :')))
    aluno.append(int(input('Digite a nota 1 :')))
    aluno.append(int(input('Digite a nota 2 :')))
    
    opcao = str(input('Deseja continuar ? [S/N]:').lower())
    
    alunos.append(aluno[:])
    
    if opcao == 'n' :
        break
        

while True:
    print('='*35) 
    print('{:<2}  {:^20s}  {:>5}'.format('N0','Nomes','Media')) 
    print('='*35) 
    for c in range(0,len(alunos)) :
        print('{:<2}  {:^20s}  {:>}'.format(c,alunos[c][0],(alunos[c][1]+alunos[c][2])/2))  
    print('='*30)
    opcao = int(input('Deseja ver a nota de qual aluno :'))
    if opcao <= len(alunos):
        print('Notas do(a)',alunos[opcao][0])
        print('Nota 1 :',alunos[opcao][1])
        print('Nota 2 :',alunos[opcao][2])
    else :
        print('Aluno invalido ,esse numero digitado nao corresponde a nenhum aluno da lista')
        
    continuar = input('Deseja continuar ? press espaço:')
    
    os.system('clear')
    
    if continuar != '':
        break
    
    
        
    
    
    
    

    