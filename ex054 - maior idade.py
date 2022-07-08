#importar datatime para calculo
from datetime import datetime
#entrada de 7 datas com um laço for #logica com saide demaiores de 18 anos
idade = 0
cont = 0
hoje = datetime.now()

for c in range(0, 7):
    nasc = int(input('\033[1:34mInforme ano nascimento: \033[m'))
    idade = hoje.year - nasc
    if idade >= 21:
        cont += 1
print('{} são maiores de idade!'.format(cont))