import datetime

print("Digite a sua idade no formato Dia/Mes/Ano")

idade = input(":")

data = str(datetime.date.today())

mes = int(data[data.find("-")+1:data.rfind("-")])

ano = int(data[:data.find("-")])

mes_idade = int(idade[idade.find("/")+1:idade.rfind("/")])

ano_idade = int(idade[idade.rfind("/")+1:])

atraso_anual= 0
atraso_mensal = mes 

if (ano-ano_idade) > 18 :
    atraso_anual = (ano - ano_idade) - 18
    if mes_idade < mes :
            atraso_mensal = mes - mes_idade
            
    print("""Voce ja passou  do tempo de alistamento 
Voce esta a :
{} anos 
{} meses  
atrasado""".format(atraso_anual,atraso_mensal))
    
if(ano-ano_idade) == 18 :
    if mes_idade < mes :
        print("""Voce ja passou  do tempo de alistamento 
Voce esta a :
{} meses atrasado""".format(mes - mes_idade))
    else : 
        opcao = input("Ja é hora de se alistar faltam {} meses para o alistamento o link para agilizar ? S/N :".format(mes_idade-mes))
        if opcao == "S" :
            print("https://alistamento.eb.mil.br/")
        

if(ano-ano_idade) < 18 :
    print("""Ainda vai se alistar ainda tem bastante tempo de se alistar.
Faltam {} anos e {} meses para o alistamento.""".format((18 - (ano-ano_idade)),mes))
            