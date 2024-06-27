qtdDias = float(input("Informe a quantidade de dias utilizados: "))
qtdKm = float(input("Informe a quantidade de quilometros rodados: "))

print("O preço a ser pago é de Rs{:.2f}".format(((qtdDias * 60) + (qtdKm * 0.15))))