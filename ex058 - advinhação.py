print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
numero = int(input('Escolha um numero de 0 a 10: '))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
tentativas = 1
from random import randint
comp = randint(0, 10)
while numero != comp:
    print(f'Você {numero} e computador {comp}!')
    numero = int(input('Tente novamente...\nNumero de 0 a 10:'))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    tentativas += 1
    comp = randint(0, 10)
if numero == comp:
    print(f'Parabéns você acertou!\nVocê {numero} e computador {comp}!')
print(f'\033[;33mVocê tentou {tentativas} vezes até acertar!')
