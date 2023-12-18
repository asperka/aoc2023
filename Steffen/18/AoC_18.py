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

dirs ={'R': (1,0), 'L': (-1,0), 'U': (0,-1), 'D': (0,1)}

def move(pos, dir):
    return (pos[0]+dir[0], pos[1]+dir[1])

def print_grid(grid):
    for line in grid:
        for c in line:
            print (c, end=' ')
        print()

positions = [(0,0)]
pos = (0,0)
min_pos = (0,0)
max_pos = (0,0)

for line in lines:
    m = re.match('([RLUD]) (\d+) ', line)
    dir = m.group(1)
    steps = int(m.group(2))
    for _ in range(steps):
        pos = move(pos, dirs[dir])
        positions.append(pos)
        min_pos = (min(min_pos[0], pos[0]), min(min_pos[1], pos[1]))
        max_pos = (max(max_pos[0], pos[0]), max(max_pos[1], pos[1]))

grid = []
for _ in range(max_pos[1] - min_pos[1] + 3):
    grid.append(list('.'*(max_pos[0]-min_pos[0]+3)))

min_pos = (min_pos[0]-1, min_pos[1]-1)
print(min_pos, max_pos)
print(len(grid[0]), len(grid))

for pos in positions:
    (x, y) = (pos[0]-min_pos[0], pos[1]-min_pos[1])
    grid[y][x] = '#'

print_grid (grid)
start_pos = None
for y, line in enumerate(grid):
    text = ''.join(line)
    x = text.find('.#.')
    if x>=0:
        start_pos = (x+2,y)
        break
print (start_pos)

stack = [start_pos]
while len(stack)>0:
    pos = stack.pop(0)
    for d in dirs.values():
        p = (d[0]+pos[0], d[1]+pos[1])   
        if grid[p[1]][p[0]] == '.':
            stack.append(p)
        grid[p[1]][p[0]] = '#'

print_grid (grid)

cubes = [line.count('#') for line in grid]
print(sum(cubes))