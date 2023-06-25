print("-=+=-" * 20)
print("Construtor de Triangulos")
print("-=+=-" * 20)
r1 = float(input("Primeira medida: "))
r2 = float(input("Segunda medida: "))
r3 = float(input("Terceira medida: "))

## Construção ##
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Essas medidas PODEM FORMAR um Triangulo.")
else:
    print("Essas medidas NÃO PODEM FORMAR um Triangulo.")
    