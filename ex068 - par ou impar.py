numero = comp = escolha = vitorias = 0
import random

while True:
    numero = int(input('Escolha um numero[1 até 10]: '))
    comp = random.randint(1, 10)
    escolha = str(input('Par ou Impar? [P/I]')).upper()

    if (numero + comp) % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    if (escolha == 'P' and resultado == 'P') or (escolha == 'I' and resultado == 'I'):
        print(f'Você venceu !\nEscolheu {numero:-^5} e o computador {comp:-^5}!')
        vitorias += 1

    else:
        print(f'Você perdeu!\nEscolheu {numero:-^5} e o computador {comp:-^5}!')
        print(f'Você ganhou {vitorias:-^5} vezes!')
        break
print('Volte sempre!')
