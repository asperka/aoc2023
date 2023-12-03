# -*- coding: utf-8 -*-

import re

text="""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
text = open("input.txt").read()

lines = text.split()
lines = list(filter(None, lines))

# add border of '.'
empty_line = '.' * len(lines[0])
lines = [empty_line] + lines + [empty_line]
for i in range(len(lines)):
    lines[i] = '.' + lines[i] + '.'

gears = {}
def is_gear(i,x):
    return lines[i][x] == '*'
def add_gear(i,x,nr):
    if not (i,x) in gears:
        gears[(i,x)] = []
    gears[(i,x)].append(int(nr))

sum = 0
nr_lines = []
for l in lines:
    nr_lines.append(re.findall('\d+', l))
for i in range(len(nr_lines)):
    end = 0
    for nr in nr_lines[i]:
        start = lines[i].find(nr, end)-1
        end = start + len(nr)+1
        if is_gear(i,start):
            add_gear(i,start,nr)
        if is_gear(i,end):
            add_gear(i,end,nr)
        for x in range(start, end+1):
            if is_gear(i-1,x):
                add_gear(i-1,x,nr)
            if is_gear(i+1,x):
                add_gear(i+1,x,nr)

#print (gears)
for g in list(gears.values()):
    if len(g) == 2:
        sum += g[0]*g[1]
print (sum)