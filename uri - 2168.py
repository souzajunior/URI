n = int(input())

matriz = []
cont = 0
for i in range (n+1):
        entrarda = list(map(int,input().split()))
        matriz.append(entrarda)
    
for i in range(n):
    for j in range(n):
        if matriz[i][j] == 1:
            cont += 1 
        if matriz[i+1][j] == 1:
            cont += 1 
        if matriz[i][j+1] == 1:
            cont += 1 
        if matriz[i+1][j+1] == 1:
            cont+= 1 
            
        if cont >=2:
            print("S", end='')
        else:
            print("U", end = '')
        cont = 0
    print()
