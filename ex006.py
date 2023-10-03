num = int(input("Digite um numero: "))
print(
    "O dobro de {} eh {}\nO triplo de {} eh {}\nA raiz quadrada de {} eh {:.2f}\n".format(
        num, (num * 2), num, (num * 3), num, ((num ** (1 / 2)))
    )
)
