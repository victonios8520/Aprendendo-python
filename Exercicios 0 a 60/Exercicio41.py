import datetime

ano = str(datetime.date.today())

ano = (ano[:ano.find("-")])

ano_nascimento = int(input("Digite o ano de seu nascimento :"))

data = int(ano) - ano_nascimento 

print("Classificação :")
if data <= 9:
    print("MIRIM")
elif 9 < data <= 14 :
    print("INFANTIL")
elif 14 < data <= 19 :
    print("Junior")
elif 19 < data <= 20:
    print("SÉNIOR")
else :
    print("MASTER")