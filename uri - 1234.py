while True:
    try:
        entrada = input()
        nova_entrada = ''
        aux = 0
        for i in entrada:
            if (i == ' '):
                nova_entrada += i
                continue
            if (aux == 0):
                nova_entrada += i.upper()
                aux += 1
            else:
                nova_entrada += i.lower()
                aux = 0

        print(nova_entrada)

    except EOFError:
        break