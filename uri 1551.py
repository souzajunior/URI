N = int(input())

total = 2847
metade_total = total/2

for i in range(N):
    total_digitado = 0
    entrada = input()
    entrada = list(set(entrada))
    for j in entrada:
        if ('a' <= j <= 'z'):
            total_digitado += ord(j)
        else:
            continue
    
    if ((total_digitado >= metade_total) and (total_digitado < total)):
        print('frase quase completa')
    elif (total_digitado >= total):
        print('frase completa')
    elif (total_digitado < metade_total):
        print('frase mal elaborada')
