# -*- coding: utf-8 -*-
m = 1000000007

pots = [0] * 1001

def calculaPots():
  pot = 1
  rest = 1000
  i = 1
  pots[0] = 1

  while rest > 0:
    pot = (pot * 26) % m
    pots[i] = pot
    rest -= 1
    i += 1  
  
  
calculaPots()

while True:
  resposta = 0
  try:
    palavra = str(input())    
    cont = len(palavra)  
    for i in range(cont):
      resposta += ((ord(palavra[i]) - 65) * pots[cont - i - 1]) % m
      resposta %= m      

    print(resposta)

  except EOFError:
    break