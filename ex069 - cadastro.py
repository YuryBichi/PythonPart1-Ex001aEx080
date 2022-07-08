mais18 = homens = mulheresadultas = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).upper().strip()
    continuar = str(input('Continuar? [S/N]')).upper().strip()
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade >= 20:
        mulheresadultas += 1
    if continuar == 'N':
        break
print(f'São {mais18} maiores de idade!\nSão {homens} homens!\nSão {mulheresadultas} mulheres maiores de 20!')
