import string
from itertools import product


def patente():
    letras = [j for j in list(string.ascii_uppercase)]
    numeros = [i for i in list(string.digits)]
    
    total = 0
    for i in product(letras, letras, numeros, numeros, numeros, letras, letras, repeat=1):
        print(i)
        total += 1
    print(total)


patente()
