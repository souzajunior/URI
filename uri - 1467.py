while True:
    try:
        entrada = list(map(int, input().split()))
        ganhador = '*'
        if (entrada.count(1) == 1):
            if (entrada.index(1) == 0):
                ganhador = 'A'
            elif (entrada.index(1) == 1):
                ganhador = 'B'
            else:
                ganhador = 'C'
        elif (entrada.count(0) == 1):
            if (entrada.index(0) == 0):
                ganhador = 'A'
            elif (entrada.index(0) == 1):
                ganhador = 'B'
            else:
                ganhador = 'C'

        print(ganhador)
    except EOFError:
        break