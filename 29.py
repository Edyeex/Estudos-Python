velocidade = float(input("Qual era a velocidade do carro? "))
limite = int(input("Qula é o limite de velocidade? "))
mul = float(input("Qual o valor da multa por KM excedido? "))
if velocidade > limite:
    print("VOCÊ FOI MULTADO!!!\nVocê excedeu o limite de velocidade permitida que é {}".format(limite))
    multa = (velocidade - limite) * mul
    print("Você deve pagar R${:.2f} de multa".format(multa))
else:
    print("Você não foi multado\n tudo certo")
