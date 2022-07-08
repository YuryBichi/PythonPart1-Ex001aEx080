p = int(input('Primeiro termo: '))
r = int(input('Informe a razão: '))
u = p + 10 * r
for c in range(p, u, r):
    print(c)
