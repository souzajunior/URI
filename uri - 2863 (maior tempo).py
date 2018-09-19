while True:
    try:
        n = int(input())
        lista = []
        for i in range(n):
            entrada = float(input())
            lista.append(entrada)
        print(min(lista))
    except EOFError:
        break