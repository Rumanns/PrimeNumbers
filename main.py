# Title: Prime Numbers
# Objective: Verify Prime Numbers
# Date: 05/01/2021
# Author: José Valdeir

"""primos = [2]
pos = 0
n = 2
while n < 100:
    n += 1
    primos.append(n)
    if n % primos[pos]:
        print(primos)
"""
'''    if n % primos[n] != 0:
        primos.append(n)
    print(primos)
'''


'''    while n % primos[pos] != 0:
        c -= 1
    else:
        if c == 1:
            print(n, 'é primo!')
        else:
            print(n, 'não é primo')
    pos += 1
'''



#Programa 1 - Totalmente bem sucedido! Mas lento - Acima estão as tentativas de fazer um mais eficiente.
#Maior número primo existente: (2**(82.589.933))-1
n = 10000001
while 10000000 < n < 10000100:
    n += 1
    if n % 2 != 0:
        c = (n-1)/2
        while n % c != 0:
            c -= 1
        else:
            if c == 1:
                print(n, 'é primo!')
            else:
                print(n, 'não é primo')
