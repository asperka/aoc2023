# -*- coding: utf-8 -*-

import re
import numpy as np

text="""\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
text = open("input.txt").read()

lines = list(filter(None, text.split('\n')))

instructions = lines[0]
map = {}
for l in lines[1:]:
    m = re.match('(\w+) = \((\w+), (\w+)\)', l)
    map[m.group(1)] = (m.group(2), m.group(3))
#print (map)

pos = 'AAA'
step = 0
while True:
    i = instructions[step % len(instructions)]
    p = map[pos]
    if i == 'L':
        pos = p[0]
    else:
        pos = p[1]
    step += 1
    #print (step, pos)
    if pos == 'ZZZ':
        break

print (step)