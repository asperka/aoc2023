# -*- coding: utf-8 -*-

from functools import cache
import re

text="""
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""
text = open("input.txt").read()

lines = text.split('\n')
lines = list(filter(None, lines))

startx, starty = (0,0)
grid = []
grid.append(list('#' * (len(lines[0])+2)))
for line in lines:
    g = ['#']
    g.extend(list(line))
    g.append('#')
    grid.append(g)
grid.append(list('#' * (len(lines[0])+2)))

def print_grid(visited=set()):
    for y,g in enumerate(grid):
        for x,c in enumerate(g):
            if visited is not None and (x,y) in visited:
                print('O', end=' ')
            else:
                print(c, end=' ')
        print()

for y,g in enumerate(grid):
    try:
        x = g.index('S')
        if x>0:
            startx, starty = (x,y)
            g[x] = '.'
    except:
        pass

#print_grid()
print (startx,starty)

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
targets = set()

@cache
def move(x,y,steps):
    if steps == 0:
        targets.add((x,y))
        return
    for d in dirs:
        x1,y1 = x+d[0], y+d[1]
        if grid[y1][x1] != '#':
            move(x1,y1,steps-1)

target_steps = 64
move(startx, starty, target_steps)

print(len(targets))
#print_grid(targets)