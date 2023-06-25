from math import hypot
n1 = float(input('Qual é o comprimento do cateto oposto? '))
n2 = float(input('Qual é o comprimento do cateto adjacente? '))
hi = hypot(n1, n2)
print('A hipotenusa vai medir {:.2f}.'.format(hi))
