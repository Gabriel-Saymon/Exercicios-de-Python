msg = input("Digite algo: ")
print("O tipo primitivo desse valor e {}".format(type(msg)))
print("So tem espacos? {}".format(msg.isspace()))
print("E numerico? {}".format(msg.isnumeric()))
print("E alfabetico? {}".format(msg.isalpha()))
print("E alfanumerico? {}".format(msg.isalnum()))
print("Esta em maiusculas? {}".format(msg.isupper()))
print("Esta em minusculas? {}".format(msg.islower()))
print("Esta capitalizada? {}".format(msg.istitle()))
