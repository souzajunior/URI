while True:
    try:
        entrada = input()
        nova_entrada = ''

        entrada = entrada.replace(',', '')
        entrada = entrada.replace(' ', '')

        if (entrada.isnumeric()):
            if (int(entrada) > 2147483647):
                entrada = ''

        for i in entrada:
            if ((i == 'O') or (i == 'o')):
                nova_entrada += '0'
                continue
            elif (i == 'l'):
                nova_entrada += '1'
                continue
            elif (i.isnumeric()):
                nova_entrada += i
            elif (i.isalpha()):
                nova_entrada = ''
                break
            else:
                nova_entrada = ''
                break

        if (nova_entrada == ''):
            print('error')
        else:
            if (nova_entrada.isnumeric()):
                if (int(nova_entrada) > 2147483647):
                    print('error')
                else:
                    print(str(int(nova_entrada)))
            else:
                print(nova_entrada)

    except EOFError:
        break