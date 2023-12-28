# -*- coding: utf-8 -*-

from functools import cache
import re

text="""
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""
text = open("input.txt").read()

lines = text.split('\n')
lines = list(filter(None, lines))

grid = {}

class Brick:
    def __init__(self, nr, text):
        self.nr = nr
        m = re.match('(-?\d+),(-?\d+),(-?\d+)~(-?\d+),(-?\d+),(-?\d+)', text)
        x1,y1,z1 = int(m.group(1)),int(m.group(2)),int(m.group(3))
        x2,y2,z2 = int(m.group(4)),int(m.group(5)),int(m.group(6))
        dx,dy,dz = x2-x1, y2-y1, z2-z1
        nrCubes = max(dx,dy,dz) + 1
        if dx!=0:
            dx = dx/abs(dx)
        if dy!=0:
            dy = dy/abs(dy)
        if dz!=0:
            dz = dz/abs(dz)
        self.cubes = []
        for i in range(nrCubes):
            c = (int(x1+i*dx), int(y1+i*dy), int(z1+i*dz))
            self.cubes.append( c )
            grid[c] = self.nr
    def can_move_down(self):
        for c in self.cubes:
            if c[2] == 1:
                return False
            pos = (c[0],c[1],c[2]-1)
            if pos in grid and grid[pos]!=self.nr:
                return False
        return True

    def move_down(self):
        new_cubes = []
        for c in self.cubes:
            nc = (c[0], c[1], c[2]-1)
            grid[nc] = self.nr
            new_cubes.append(nc)
        for c in self.cubes:
            del grid[c]
        self.cubes = new_cubes
        for c in self.cubes:
            grid[c]=self.nr
    def remove_from_grid(self):
        for c in self.cubes:
            del grid[c]

    def is_supporting(self):
        result = set()
        for c in self.cubes:
            pos = (c[0],c[1],c[2]+1)
            if pos in grid and grid[pos]!=self.nr:
                result.add(grid[pos])
        return result
    def is_supported(self):
        result = set()
        for c in self.cubes:
            pos = (c[0],c[1],c[2]-1)
            if pos in grid and grid[pos]!=self.nr:
                result.add(grid[pos])
        return result

bricks = {}
for nr, line in enumerate(lines):
    b = Brick(nr, line)
    #print(line, b.cubes)
    bricks[nr] = b

#print()
#print(grid)

falling = True
while falling:
    falling = False
    for b in bricks.values():
        if b.can_move_down():
            falling = True
            b.move_down()

#for b in bricks.values():
    #print(b.nr, b.cubes, b.is_supporting(), b.is_supported())

#print(grid)

cnt = 0
for nr, brick in bricks.items():
    cnt_b = 0
    old_grid = grid.copy()
    brick.remove_from_grid()
    #print(f'\nremove brick {nr} from grid, {grid}')
    falling = True
    fallen = set()
    while falling:
        falling = False
        for b in bricks.values():
            if b.nr != nr and b.nr not in fallen:
                if b.can_move_down():
                    b.remove_from_grid()
                    #print(f'\nremove falling brick {b.nr} from grid => {grid}')
                    cnt_b +=1
                    falling = True
                    fallen.add(b.nr)
    #print (nr, cnt_b)
    cnt += cnt_b
    grid = old_grid
print(cnt)
