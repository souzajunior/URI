#-------------------------------------------------------------------------------
# Name:        uri 1157
# Purpose:
#
# Author:      Junior
#
# Created:     04/06/2018
# Copyright:   (c) Junior 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

N = int(input())
lista_divisores = []
for i in range(1,N+1):
    if(N % i == 0):
        lista_divisores.append(i)

for j in lista_divisores:
    print(j)
