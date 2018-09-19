'''
while True:
    x, y = input().split()
    if x == "0" and y == "0":
        break
    novaNum = ""
    for i in y:
        if i == x:
            continue
        novaNum = novaNum + i

    if novaNum.count('0') == len(novaNum) or novaNum == "":
        print(0)
    else:
        print(int(novaNum))
'''

while True:
    x, y = input().split()
    if (x == "0" and y == "0"):
        break
    for i in y:
        if (i == x):
            y = y.replace(x,'')
    if (len(y) == 0):
        print(0)
    else:
        print(int(y))
