# Title: Prime Numbers
# Objective: Verify Prime Numbers
# Date: 05/01/2021
# Author: José Valdeir

#Programa 1 - Totalmente bem sucedido! Mas lento porque divide por cada número a partir de 2.
#E no momento estou desenvolvendo outro mais eficiente que faça a divisão de cada número de um intervalor apenas pelos números primos e não por cada número até o valor máximo.
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
