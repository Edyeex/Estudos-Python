n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

## Verifica o menor valor##
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

## Verifica o maior valor ##
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior =n3 
## Resultado ##
print("Os valores que você digitou foram \033[1;33m{}, {}, {}\033[m:".format(n1, n2, n3))
print("O menor valor foi: \033[1;31m{}\033[m".format(menor))
print("O maior valor foi: \033[1;34m{}\033[m".format(maior))
