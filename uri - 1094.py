N = int(input())
qntd_cobaia = coelhos = ratos = sapos = 0

for i in range(N):
    entrada = input().split()
    qntd_cobaia += int(entrada[0])

    if (entrada[1] == 'C'):
        coelhos += int(entrada[0])
    elif (entrada[1] == 'S'):
        sapos += int(entrada[0])
    else:
        ratos += int(entrada[0])



pct_coelhos = (coelhos * 100)/qntd_cobaia
pct_ratos = (ratos * 100)/qntd_cobaia
pct_sapos = (sapos * 100)/qntd_cobaia

print('Total: {} cobaias'.format(qntd_cobaia))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format(pct_coelhos))
print('Percentual de ratos: {:.2f} %'.format(pct_ratos))
print('Percentual de sapos: {:.2f} %'.format(pct_sapos))

