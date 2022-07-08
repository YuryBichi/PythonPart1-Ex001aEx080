print('\033[;31mLaço de Tabuada!')
numero = cont = logica = 0
while True:
    numero = int(input('Digite a tabuada que deseja ver [Menor que 0 cancelar]: '))
    if numero < 0:
        break
    for cont in range(1, 11):
        logica = numero * cont
        print(f'{numero} x {cont} = {logica}')

print('\033[;45mPROGRAMA TABUADA ENCERRADO\033[m')
