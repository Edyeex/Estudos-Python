salario = float(input("Qual é salario do funcionario \033[1;32m R$ \033[m"))
## Calcula o salario ##
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

## Resultado ##
print("Quem ganhava \033[1;32m R${:.2f}\033[m, passa a ganhar \033[1;32m R${:.2f}\033[m.".format(salario, novo))