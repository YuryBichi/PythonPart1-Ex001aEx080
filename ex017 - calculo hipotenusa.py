# ----- Metodo matematico de fazer #
co = float(input('Digite o cateto oposto:  '))
ca = float(input('Digite o cateto adjacente:  '))
# Hipotenusa é igual a raiz quadrada da soma dos quadrada dos catetos #
hi = (co**2 + ca**2) ** (1/2)
print('A hipotenusa é {:.4f}'.format(hi))


# ----- Metodo com importação #
import math
co = float(input('Digite o comprimento do cateto oposto:  '))
ca = float(input('Digite o comprimento do cateto adjacente:  '))
hi = math.hypot(ca, co)
print('A hipotenusa é {:.2f}'.format(hi))
