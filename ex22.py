from random import shuffle
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('O primeiro escolhido será:') 
print(lista)