A,B = map(float, input().split())

prc = ((B * 100)/A) - 100

print('{:.2f}%'.format(prc))
