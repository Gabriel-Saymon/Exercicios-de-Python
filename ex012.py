produto = float(input("Qual o preco do produto? R$ "))
print(
    "O produto que custava R$ {:.2f} voce pode comprar U${:.2f}".format(
        produto, produto - (produto * 0.05)
    )
)
