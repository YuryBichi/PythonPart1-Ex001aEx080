nasc = int(input('Informe seu ano de nascimento: '))
from datetime import datetime
atual = datetime.now()
idade = atual.year - nasc
if idade == 18:
    print('Hora de se alistar!')
elif idade < 18:
    print('Falta {} anos para se alistar !'.format(18 - idade))
elif idade > 18:
    print('Já passou o seu alistamento em {} anos !'.format(idade - 18))
