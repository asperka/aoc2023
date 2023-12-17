# -*- coding: utf-8 -*-

import re

text="""
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
text = open("input.txt").read()

lines = text.split('\n')
lines = list(filter(None, lines))

rocks = []
for x in range (len(lines[0])):
    str = ''
    for y in range(len(lines)):
        str += lines[y][x]
    rocks.append(str)
print (rocks)
load = []
for r in rocks:
    while r.find('.O') > -1:
        r = r.replace('.O', 'O.')
    l = 0
    for x in range(len(r)):
        if r[-(x+1)] == 'O':
            l += x+1
    load.append(l)
#print (load)
print (sum(load))

load = 0
