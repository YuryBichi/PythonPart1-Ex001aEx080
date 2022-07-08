print('\033[;33m~~~~~~~~~~~~~~~~~~~~~~\033[m\nTratando valores !\n\033[;33m~~~~~~~~~~~~~~~~~~~~~~\033[m')
soma = numeros = cont = 0

while True:

    numeros = int(input('Digite um numero [999 para parar]: '))
    if numeros == 999:
        break
    cont += 1
    soma += numeros
print(f'Você digitou {cont} números e a soma deles é {soma} !')
