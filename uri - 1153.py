'''
N = int(input())
fat = 1
for i in range(1,N+1):
    fat *= i
print(fat)
'''

import math

N = int(input())

print(math.factorial(N))
