contador = int(input())
for c in range(contador):
  entrada = input()
  caractere1 = int(entrada[0])
  caractere2 = entrada[1]
  caractere3 = int(entrada[2])
  if caractere1 == caractere3:
    print(caractere1 * caractere3)
  elif caractere2.isupper():
    print(caractere3 - caractere1)
  elif caractere2.islower():
    print(caractere1 + caractere3)
  