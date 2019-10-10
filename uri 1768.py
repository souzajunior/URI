# -*- coding: utf-8 -*-

import math

while True:
    try:
        n = int(input())
        qtd = math.ceil(n/2)
        ant = 1
        for i in range(qtd):
            print("{}{}".format(" " * int((n-ant)/2), ("*" * ant)))

            ant += 2

        print("{}*".format(" " * int((n-1)/2)))
        print("{}***".format(" " * int((n-3)/2)))

        print()
    except:
        break
