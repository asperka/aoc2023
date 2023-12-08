# -*- coding: utf-8 -*-

import re
import math

text="""\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
text = open("input.txt").read()

lines = list(filter(None, text.split('\n')))

instructions = lines[0]
map = {}
for l in lines[1:]:
    m = re.match('(\w+) = \((\w+), (\w+)\)', l)
    map[m.group(1)] = (m.group(2), m.group(3))

def get_next_pos(pos, i):
    p = map[pos]
    if i == 'L':
        return p[0]
    else:
        return p[1]
    
def count_steps(p):
    step = 0
    while True:
        i = instructions[step % len(instructions)]
        p = get_next_pos(p, i)
        step += 1
        if p[-1] == 'Z':
            return step

pos = [v for v in map.keys() if v[-1] == 'A']
print (pos)
steps = [count_steps(p) for p in pos]
print (steps)
print (math.lcm(*steps))
