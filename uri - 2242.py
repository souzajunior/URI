vogais = 'aeiou'

risada = str(input())

aux = ''

for c in risada:
  if c in vogais:
    aux += c


if aux == aux[::-1]:
  print('S')
else: 
  print('N')