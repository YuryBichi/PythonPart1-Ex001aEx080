print('-=-=-=-=-=-=-=-=\nGerador de P.A !\n-=-=-=-=-=-=-=-=')

ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A: '))
cont = 1
dezprimeiros = 10
while True:
    termo = ptermo + (cont - 1) * razao
    print(termo, end=' -> ' if cont < dezprimeiros else ' PAUSA')
    cont += 1
    if cont > dezprimeiros:
        numero = int(input('\nQuantos termos voce quer mostrar mais? '))
        dezprimeiros += numero
        if numero == 0:
            break

print(f'Progressão finalizada com {dezprimeiros+numero} termos !')
