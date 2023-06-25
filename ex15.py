salario = float(input('Qual é o salário do funcionário? R$'))
aumento = float(input('Quanto de aumento o funcionario vai receber? %'))
novo = salario + (salario * aumento / 100)
print ('Um funcionario que ganhava R${:.2f}, com o aumento de {}%, passa a receber R${:.2f}'.format(salario, aumento, novo))
