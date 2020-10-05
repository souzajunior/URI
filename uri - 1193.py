# decimal para binario
def decToBin(n):
  return '{:b}'.format(int(n))

# binário para decimal
def binToDec(n):
  return int(str(n), 2)

# decimal para hexadecimal
def decToHex(n):
  v = str(hex(int(n)))
  return v[v.index('x') + 1:]

# hexadecimal para decimal
def hexToDec(n):
  return int(str(n), 16)

# binario para hexadecimal
def binToHex(n):
  v = hex(int(str(n), 2))
  return v[v.index('x') + 1:]

# hex to binary
def hexToBin(n):
  return decToBin(hexToDec(n))


cases = []

n = int(input())

for i in range(0, n):
  cases.append(str(input()).split(" "))


for j in range(0, len(cases)):
  x = cases[j][0]
  base = cases[j][1]

  print('Case {}:'.format(j + 1))
  if base == 'bin':
    print(binToDec(x), 'dec')
    print(binToHex(x), 'hex')
  elif base == 'dec':
    print(decToHex(x), 'hex')
    print(decToBin(x), 'bin')
  elif base == 'hex':
    print(hexToDec(x), 'dec')
    print(hexToBin(x), 'bin')
  print()