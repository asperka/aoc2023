# -*- coding: utf-8 -*-
# 18.12. 6:25

import re

text="""
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""
text = open("input.txt").read()
lines = filter(None, text.split('\n'))

#https://math.stackexchange.com/questions/492407/area-of-an-irregular-polygon

dirs ={'0': (1,0), '2': (-1,0), '3': (0,-1), '1': (0,1)}

def move(pos, dir, steps):
    return (pos[0]+dir[0]*steps, pos[1]+dir[1]*steps)

positions = [(0,0)]
pos = (0,0)
sum = 2 # corners
for line in lines:
    m = re.search('\(#(.*)([0123])\)', line)
    dir = m.group(2)
    steps = int(m.group(1), 16)
    print (dir, steps)
    pos = move(pos, dirs[dir], steps)
    positions.append(pos)
    sum += steps # border
positions.append((0,0))

for i in range(len(positions)-1):
    p0 = positions[i]
    p1 = positions[i+1]
    sum += p0[0]*p1[1]-p0[1]*p1[0]

print(sum/2)