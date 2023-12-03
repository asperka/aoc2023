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

def is_symbol(i,x):
    return lines[i][x] not in '.0123456789'

sum = 0
nr_lines = []
for l in lines:
    nr_lines.append(re.findall('\d+', l))
for i in range(len(nr_lines)):
    end = 0
    for nr in nr_lines[i]:
        start = lines[i].find(nr, end)-1
        end = start + len(nr)+1
        found = is_symbol(i,start) or is_symbol(i,end)
        for x in range(start, end+1):
            found = found or is_symbol(i-1, x)
            found = found or is_symbol(i+1, x)
        if found:
            sum += int(nr)

print (sum)