while True:
    S = input().split()[0]
    if (S == '0'):
        break
    comb = 1
    for i in range(1,len(S)+1):
        comb *= i

    print(comb)
