#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Junior
#
# Created:     04/06/2018
# Copyright:   (c) Junior 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Escreva uma função capaz de receber uma quantidade #indeterminada de parâmetros e imprima na telas os #números primos contidos nessa lista.

qntd = int(input())
for vezes in range(qntd):
    l_divisores = [] #Lista guardará os números que dividem o nosso numero

    num_verificar = int(input())
    if (num_verificar == 1): #1 não é perfeito, :)
        print('1 nao eh perfeito')
        continue

    for num in range(1,num_verificar): #Aqui percorreremos o intervalo de 1 até numero informado - 1
        if (num_verificar % num == 0): # Se o numero dividir o nosso numero a verificar, então será um divisor
            l_divisores.append(num)

    if (sum(l_divisores) == num_verificar): # Se, após verificamos os divisores, a soma dos divisores for igual ao nosso numero, entao eh perfeito
        print('%i eh perfeito'%(num_verificar))
    else:
        print('%i nao eh perfeito'%(num_verificar))

    l_divisores.clear() # Limpando a lista para outro numero a verificar