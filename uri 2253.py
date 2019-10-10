# -*- coding: utf-8 -*-

while (True):
    try:
        ent = input()

        test = True
        hasNumber = False
        hasUpper = False
        hasLower = False
        tam = len(ent)

        if tam < 6 or tam > 32: test = False
        elif not ent.isalnum(): test = False
        else:
            for i in ent:
                if i.islower(): hasLower = True
                if i.isupper(): hasUpper = True
                if i.isnumeric(): hasNumber = True

                if hasNumber and hasUpper and hasLower: break
            else:
                test = False

        resp = "Senha valida." if test else "Senha invalida."
        print(resp)
    except:
        break
