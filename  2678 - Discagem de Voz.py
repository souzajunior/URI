# -*- coding: utf-8 -*-
import string
entradas = []
teclado = ['', '', 'ABCabc', 'DEFdef', 'GHIghi', 'JKLjkl', 'MNOmno', 'PQRSpqrs', 'TUVtuv', 'WXYZwxyz']
saida = ''

while True:
    try:
        entradas.append(str(input()))        
    except EOFError:
        break

for palavra in entradas:
    for l in palavra:
        if l in string.digits or l == '*' or l == '#':
            saida+=l
        else:
            for i in range(0, len(teclado)):   
                if l in teclado[i]:
                    saida+=str(i)
    print(saida)
    saida = ''