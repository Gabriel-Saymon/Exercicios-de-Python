import math
catetoO = float(input("Comprimento do cateto oposto: "))
catetoA = float(input("Comprimento do cateto adjacente: "))
hipotenusa = math.sqrt((catetoA **2) +(catetoO **2))
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))