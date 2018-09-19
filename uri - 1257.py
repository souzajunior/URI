lista_alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

casos_testes = int(input())

for caso in range(casos_testes):
    qntd_linhas = int(input())
    total = 0
    for linha in range(qntd_linhas):
        entrada = list(input())
        for caractere in entrada:
            posicao_alfabeto = lista_alfabeto.index(caractere)
            elemento_entrada = linha
            posicao_elemento = entrada.index(caractere)
            valor = posicao_alfabeto + elemento_entrada + posicao_elemento
            total += valor
            entrada[posicao_elemento] = ''
    print(total)


