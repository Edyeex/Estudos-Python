larg = float(input('Qual a largura da parede ? '))
alt = float(input('Qual a altura da parede ? '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {} metros quadrados.'.format(larg, alt, area))
tinta = area / 2
print('para pintar uma parede de {} metros quadrados você vai precisar de {} Litros de tinta.'.format(area, tinta))