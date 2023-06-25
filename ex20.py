from math import radians, sin, cos, tan
an = float(input('Digite um angulo: '))
seno = sin(radians(an))
print('O angulo {} tem o SENO de {:.2f}.'.format(an, seno))
cosseno = cos(radians(an))
print('O angulo {} tem o COSSENO de {:.2f}.'.format(an, cosseno))
tangente = tan(radians(an))
print('O angulo {} tem a TANGENTE de {:.2f}.'.format(an, tangente))