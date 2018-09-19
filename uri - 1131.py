novo_grenal = 1
vit_inter = vit_grem = empates = 0
grenais = 0
while (novo_grenal == 1):
    gol_inter, gol_grem = map(int, input().split())
    grenais += 1

    if (gol_inter > gol_grem):
        vit_inter += 1
    elif (gol_inter < gol_grem):
        vit_grem += 1
    else:
        empates += 1

    print('Novo grenal (1-sim 2-nao)')
    novo_grenal = int(input())

if (vit_inter > vit_grem):
    vencedor = 'Inter'
else:
    vencedor = 'Gremio'
print('{} grenais'.format(grenais))
print('Inter:{}'.format(vit_inter))
print('Gremio:{}'.format(vit_grem))
print('Empates:{}'.format(empates))
print('{} venceu mais'.format(vencedor))
