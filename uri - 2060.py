n = int(input())
numeros = list(map(int, input().split()))
tot_2 = tot_3 = tot_4 = tot_5 = 0

for i in numeros:
    if (i % 2 == 0):
        tot_2 += 1
    if (i % 3 == 0):
        tot_3 += 1
    if (i % 4 == 0):
        tot_4 += 1
    if (i % 5 == 0):
        tot_5 += 1

print('{} Multiplo(s) de 2'.format(tot_2))
print('{} Multiplo(s) de 3'.format(tot_3))
print('{} Multiplo(s) de 4'.format(tot_4))
print('{} Multiplo(s) de 5'.format(tot_5))


