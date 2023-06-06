import random

baixo = "abcdefghijklmnopqrstuvwxyz"
alto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "[]{}()*;/,._-"

all = baixo + alto + numeros + simbolos
length = 16
senha = "".join(random.sample(all,length))

print(senha)




