# -*- coding: utf-8 -*-

import re
import numpy as np

text="""\
.................
.F--------7......
.L-------7|......
.S7......||......
.||......||F7....
.|L------J|J|F7..
.L--------J..LJ|..
.|..|.|.......L7.
.L--J.L--------J.
.................
"""

text="""\
.................
.F--------7......
.|F------7|......
.||......||......
.||......||F7....
.|L-7.S--JLJ|F7..
.|..|.|.....LJ|..
.|..|.|.......L7.
.L--J.L--------J.
.................
"""

# text = """\
# .F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ...
# """

# text = """\
# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# """

text = open("input.txt").read()
lines = list(filter(None, text.split('\n')))

def add_border(lines):
    # add border of '.'
    empty_line = '.' * len(lines[0])
    lines = [empty_line] + lines + [empty_line]
    for i in range(len(lines)):
        lines[i] = list('.' + lines[i] + '.')
    return lines

def line_as_text(l):
    s = ''
    for c in l:
        s+=c
    return s

def print_grid(grid):
    [print(line_as_text(l)) for l in grid]

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
connections = { 
'|': [north, south],
'-': [east, west],
'L': [north, west],
'J': [east, north],
'7': [west, south],
'F': [east, south],
'.': [],
}

lines = add_border(lines)
#print_grid(lines)

def move_pos(pos, dir):
    return (pos[0]+dir[0], pos[1]+dir[1])

def element_at(grid, pos):
    return grid[pos[1]][pos[0]]

start_pos = (0,0)
for x in range(len(lines[0])):
    for y in range(len(lines)):
        if element_at(lines, (x,y)) == 'S':
            start_pos = (x, y)
print (start_pos)

def mark_loop(grid, pos):
    grid[pos[1]][pos[0]] = '*'

def find_start(grid, pos, dir):
    nrSteps = 1
    while element_at(lines, pos) != 'S':
        mark_loop(grid, pos)
        #print (pos, dir, element_at(pos), dirs[element_at(pos)])
        nrSteps += 1
        if not dir in dirs[element_at(lines, pos)]:
            return -1
        dir = dirs[element_at(lines, pos)][dir]
        pos = move_pos(pos, dir)
        if element_at(lines, pos) == '.':
            return -1
    return nrSteps/2

def create_grid():
    for d in [north, east, west, south]:
        grid = [['.' for i in lines[0]] for l in lines]
        mark_loop(grid, start_pos)
        p = element_at(lines, move_pos(start_pos, d))
        #print (p, d, dirs[p])
        if d in dirs[p]:
            nrSteps = find_start(grid, move_pos(start_pos, d), d) 
            if nrSteps > 0:
                return grid
        
grid = create_grid()
#print_grid(grid)
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if element_at(grid, (x,y)) == '.':
            lines[y][x] = '.'

e = element_at(lines, move_pos(start_pos, east))
w = element_at(lines, move_pos(start_pos, west))
n = element_at(lines, move_pos(start_pos, north))
s = element_at(lines, move_pos(start_pos, south))

if west in connections[e] and east in connections[w]:
    s = '-'
if north in connections[s] and south in connections[s]:
    s = '|'
if west in connections[e] and north in connections[s]:
    s = 'F'
if west in connections[e] and south in connections[n]:
    s = 'L'
if east in connections[w] and south in connections[n]:
    s = 'J'
if east in connections[w] and north in connections[s]:
    s = '7'

lines[start_pos[1]][start_pos[0]] = s
#print_grid(lines)

for y in range(len(grid)):
    for xp in range(len(grid[0])):
        p = (xp,y)
        if element_at(grid, p) == '*':
            continue
        if grid[y][:xp].count('.') != xp:
            cnt = 0
            x = xp
            l0 = line_as_text(lines[y][xp:])
            l = l0.replace('-', '')
            l = l.replace('FJ', '|')
            l = l.replace('L7', '|')
            cnt = l.count('|')
            if cnt % 2 == 1:
                grid[y][xp] = 'I'

#print_grid(grid)
nr_inner = sum([l.count('I') for l in grid])
print (nr_inner)

