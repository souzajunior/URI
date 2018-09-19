# Problema está dando wrong answer, não localizei o motivo ainda
casos_teste = int(input())

for i in range(casos_teste):
    num_instrucao = int(input())
    posicao = 0
    vetor = []
    for j in range(num_instrucao):
        entrada = input()
        if (entrada[0] == 'L'):
            posicao -= 1
            vetor.append('L')
        elif (entrada[0] == 'R'):
            posicao += 1
            vetor.append('R')
        else:
            if (vetor[int(entrada[len(entrada) - 1]) -1] == 'L'):
                vetor.append('L')
                posicao -= 1
            else:
                posicao += 1
                vetor.append('R')
    print(posicao)