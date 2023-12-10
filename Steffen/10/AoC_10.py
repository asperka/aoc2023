# -*- coding: utf-8 -*-

import re
import numpy as np

text="""\
7-F7-
|FJ|7
SJLL7
|F--J
LJ.LJ
"""
text = open("input.txt").read()
lines = list(filter(None, text.split('\n')))

def add_border(lines):
    # add border of '.'
    empty_line = '.' * len(lines[0])
    lines = [empty_line] + lines + [empty_line]
    for i in range(len(lines)):
        lines[i] = '.' + lines[i] + '.'
    return lines

def print_grid(grid):
    [print(l) for l in grid]

south = (0,1)
north = (0, -1)
east = (1,0)
west = (-1,0)
dirs = { 
'|': {north: north, south:south},
'-': {east: east, west:west},
'L': {south: east, west: north},
'J': {south: west, east: north},
'7': {north: west, east: south},
'F': {north: east, west: south},
'.': {},
}

lines = add_border(lines)
print_grid(lines)

def move_pos(pos, dir):
    return (pos[0]+dir[0], pos[1]+dir[1])

def grid(pos):
    return lines[pos[1]][pos[0]]

start = (0,0)
for x in range(len(lines[0])):
    for y in range(len(lines)):
        if grid((x,y)) == 'S':
            start = (x, y)
print (start)

def find_start(pos, dir):
    nrSteps = 1
    while grid(pos) != 'S':
        #print (pos, dir, grid(pos), dirs[grid(pos)])
        nrSteps += 1
        if not dir in dirs[grid(pos)]:
            return -1
        dir = dirs[grid(pos)][dir]
        pos = move_pos(pos, dir)
        if grid(pos) == '.':
            return -1
    return nrSteps/2

for d in [north, east, west, south]:
    p = grid(move_pos(start, d))
    #print (p, d, dirs[p])
    if d in dirs[p]:
        nrSteps = find_start(move_pos(start, d), d) 
        print (d, nrSteps)