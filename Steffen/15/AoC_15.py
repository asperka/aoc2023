# -*- coding: utf-8 -*-

text="""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

#text = open("input.txt").read()
codes = text[:-1].split(',')
codes = list(filter(None, codes))

print (len(text))
print (f'"{codes[-1]}"')
def calcHASH(text):
    cv = 0
    for c in text:
        cv += ord(c)
        cv = (cv*17)%256
    return cv

print (sum(calcHASH(c) for c in codes))

