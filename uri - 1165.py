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
    num_primos = [] #Lista guardará nossos números primos
    l_divisores = [] #Lista guardará os números que dividem o nosso numero

    num_verificar = int(input())
    if (num_verificar == 1): #1 não é primo, :)
        print('1 nao eh primo')
    for num in range(1,num_verificar+1): #Aqui percorreremos o intervalo de 1 até numero informado
        if (len(l_divisores) > 2): #Se tiver mais de 2 divisores, então sairemos do laço
            break

        if (num_verificar % num == 0): # Se o numero dividir o nosso numero a verificar, então será um divisor
            l_divisores.append(num)

    if (len(l_divisores) == 2): # Se, após verificamos os divisores, for igual a 2, então temos um numero primo
        print('{0} eh primo'.format(num_verificar))
    else:
        print('{0} nao eh primo'.format(num_verificar))

    l_divisores.clear() # Limpando a lista para outro numero a verificar