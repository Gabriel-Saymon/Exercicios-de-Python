d = float(input("Digite uma distancia em metros: "))
print(
    "{}km\n{}hm\n{}am\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm\n".format(
        (d / 1000), (d / 100), (d / 10), (d * 10), (d * 100), (d * 100), (d * 1000)
    )
)
