e = []
for c in range(0,5):
    peso = float(input('\033[1;96mDigite seu peso: \033[m'))
    e.append(peso)
print('O maior é {} e o menor é {}!'.format(max(e), min(e)))