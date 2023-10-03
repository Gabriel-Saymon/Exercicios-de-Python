largura = float(input("Qual a largura da parede: "))
altura = float(input("Qual a altura da parede: "))
area = altura * largura
print(
    "A sua parede tem a dimensao de {:.2f}x{:.2f} e sua area e de {:.3f}m2\nPara pintar essa parede, voce precisara de {:.4f}l de tinta".format(
        largura, altura, area, area / 2
    )
)
