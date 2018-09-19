lista = []
while True:
    try:
        n = int(input())
        for i in range(n):
            entrada = input()
            lista.append(int('0b' + entrada, 2))

        for i in range(len(lista)):
            lista[i] = chr(lista[i])

        palavra = ''.join(lista)
        print(palavra)
        lista.clear()
    except EOFError:
        break