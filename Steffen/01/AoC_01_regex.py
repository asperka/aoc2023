# -*- coding: utf-8 -*-

text="""
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
text = open("input.txt").read()

import re

lines = text.split()
sum = 0
for l in lines:
    chars = re.findall('\d', l)
    nr = chars[0]+chars[-1]
    print (l, nr)
    sum += int(nr)
print (sum)