x = int(input())
y = int(input())
valores_finais = []
if (x > y):
    x,y = y,x

for i in range(x+1,y):
    if ((i % 5 == 2) or (i % 5 == 3)):
        valores_finais.append(i)
        
valores_finais.sort()
for x in valores_finais:
    print(x)
