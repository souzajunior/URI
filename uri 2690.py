# -*- coding: utf-8 -*-

dic = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 
    'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 0, 'l': 1,
    'm': 2, 'n': 3, 'o': 4, 'p': 5, 'q': 6, 'r': 7, 
    's': 8, 't': 9, 'u': 0, 'v': 1, 'w': 2, 'x': 3, 
    'y': 4, 'z': 5, 'A': 6, 'B': 8, 'C': 7, 'D': 5,
    'E': 2, 'F': 3, 'G': 0, 'H': 9, 'I': 1, 'J': 4,
    'K': 6, 'L': 8, 'M': 7, 'N': 5, 'O': 2, 'P': 3, 
    'Q': 0, 'R': 9, 'S': 1, 'T': 4, 'U': 6, 'V': 8, 
    'W': 7, 'X': 5, 'Y': 2, 'Z': 3 
}

n = int(input())
for i in range(n):
    out = ""
    ent = input()
    for i in ent:
        if i != " ": 
            out += str(dic[i])
            if len(out) == 12: break 
    
    print(out)
