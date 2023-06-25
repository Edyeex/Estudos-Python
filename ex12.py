real = float(input('Quanto dinheiro você tem seu pobre? R$'))
dolar = real / 5.20
euro = real / 5.53
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('E com R${:.2f} você consegue comprar em Euro €{:.2f}'.format(real, euro))
