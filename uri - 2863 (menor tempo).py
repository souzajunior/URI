while True:
    try:
        n = int(input())
        menor = 99
        for i in range(n):
            entrada = float(input())
            if (entrada < menor):
                menor = entrada
        print(menor)
    except EOFError:
        break