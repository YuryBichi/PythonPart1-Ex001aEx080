ano = int(input('Informe ano nascimento: '))
from datetime import datetime
idade = datetime.now().year - ano
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Senior')
elif idade > 20:
    print('Master')
print(idade)