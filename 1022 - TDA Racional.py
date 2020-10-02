# -*- coding: utf-8 -*-

cont = int(str(input()))
entradas = []

def mdc(m, n):
    if m % n == 0:
        return n
    else:
        return mdc(n, m % n)

def Soma(N1, D1, N2, D2):
    numerador = (N1*D2 + N2*D1)
    denominador = (D1*D2)
    m = mdc(numerador, denominador)
    return "%d/%d = %d/%d" %(numerador, denominador, (numerador/m), (denominador/m))

def Sub(N1, D1, N2, D2):
    numerador = (N1*D2 - N2*D1)
    denominador = (D1*D2)
    m = mdc(numerador, denominador)
    return "%d/%d = %d/%d" %(numerador, denominador, (numerador/m), (denominador/m))

def Mult(N1, D1, N2, D2):
    numerador = (N1*N2)
    denominador = (D1*D2)
    m = mdc(numerador, denominador)
    return "%d/%d = %d/%d" %(numerador, denominador, (numerador/m), (denominador/m))

def Div(N1, D1, N2, D2):
    numerador = (N1*D2)
    denominador = (N2*D1)
    m = mdc(numerador, denominador)
    return "%d/%d = %d/%d" %(numerador, denominador,(numerador/m), (denominador/m))

for i in range(0, cont):
    entradas.append(str(input()).split(" "))

for s in entradas:
    if s[3] == "+":
        print(Soma(int(s[0]), int(s[2]), int(s[4]), int(s[6])))
    if s[3] == "-":
        print(Sub(int(s[0]), int(s[2]), int(s[4]), int(s[6])))
    if s[3] == "*":
        print(Mult(int(s[0]), int(s[2]), int(s[4]), int(s[6])))
    if s[3] == "/":
        print(Div(int(s[0]), int(s[2]), int(s[4]), int(s[6])))