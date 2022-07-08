sexo = str(input('Digite o sexo: [M/F]')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Tente Novamente...\nDigite o sexo: [M/F]')).upper()[0].strip()
print(f'\033[;33mSexo {sexo} cadastrado com Sucesso!')
