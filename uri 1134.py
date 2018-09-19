alcool = gasolina = diesel = 0
while True:
    num = int(input())
    if ((num < 1) or (num > 4)):
        continue
    elif (num == 4):
        break
    elif (num == 1):
        alcool += 1
    elif (num == 2):
        gasolina += 1
    elif (num == 3):
        diesel += 1
print('MUITO OBRIGADO')
print('Alcool: {0}\nGasolina: {1}\nDiesel: {2}'.format(alcool,gasolina,diesel))
