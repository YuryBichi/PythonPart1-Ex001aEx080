usuario = int(input('Informe sua escolha: [1] - Pedra [2] - Papel [3] - Tesoura'))
from random import randint
from time import sleep
comp = randint(1, 3)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('JÁ')

if comp == usuario: #escolhas iguais
    print(' {} e {} - Empate'.format(comp, usuario))
elif comp == 1 and usuario == 2: #pedra e papel -1 u
    print(' {} e {} - Você venceu')
elif comp == 1 and usuario == 3: #pedra e tesoura -2 c
    print('Comp venceu')
elif comp == 2 and usuario == 3: #papel e tesoura -1 u
    print('Você venceu')
elif comp == 2 and usuario == 1: #papel e pedra 1 c
    print('Comp venceu')
elif comp == 3 and usuario == 1: #tesoura e pedra 2 u
    print('Você venceu')
elif comp == 3 and usuario == 2: # tesoura e papel 1 c
    print('Comp venceu')


