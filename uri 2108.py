maior = 0
while True:
    entrada = input().split()
    if (entrada[0] == '0'):
        break
    
    resultado_num = []   
    for i in entrada:
        if (len(i) >= maior):
            palavra_maior = i
            maior = len(i)
            
        resultado_num.append(str(len(i)))

    print('-'.join(resultado_num))

print()
print('The biggest word: {}'.format(palavra_maior))
