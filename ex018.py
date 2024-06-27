import math
angulo = float(input("Digite o Angulo que voce deseja: "))
print("O angulo de {} tem o SENO de {:.2f}\nO angulo de {} tem o COSSENO de {:.2f}\nO angulo de {} tem o TANGENTE de {:.2f}\n".format(angulo,math.sin(math.radians(angulo)), angulo, math.cos(math.radians(angulo)), angulo, math.tan(math.radians(angulo))))