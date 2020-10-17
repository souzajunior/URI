possibilidades = [4, 7, 12, 22, 52, 102, 10, 15, 25, 55, 105, 20,
    30, 60, 110, 40, 70, 120, 100, 150, 200]

while (True):
    r = "impossible"
    n, m = map(int, input().split())
    if (n == 0 and m == 0): break
    
    troco = m - n
    for i in range(21):
        if (possibilidades[i] == troco):
            r = "possible"
            break
        
    print(r)
