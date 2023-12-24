# -*- coding: utf-8 -*-

#24.12. 10:38

text="""\
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""

text = open("input.txt").read()
lines = text[:-1].split('\n')
lines = list(filter(None, lines))

next_dirs = {
    ('|', (1,0)): [(0,1), (0,-1)],
    ('|', (-1,0)): [(0,1), (0,-1)],
    ('-', (0,1)): [(1,0), (-1,0)],
    ('-', (0,-1)): [(1,0), (-1,0)],
    ('/', (1,0)): [(0,-1)],
    ('/', (-1,0)): [(0,1)],
    ('/', (0,1)): [(-1,0)],
    ('/', (0,-1)): [(1,0)],
    ('\\', (1,0)): [(0,1)],
    ('\\', (-1,0)): [(0,-1)],
    ('\\', (0,1)): [(1,0)],
    ('\\', (0,-1)): [(-1,0)],
}

max_x = len(lines[0])-1
max_y = len(lines)-1
def pos_in_grid(p):
    return 0<=p[0]<=max_x and 0<=p[1]<=max_y 

def get_next_pos(position):
    pos, dir = position
    c = lines[pos[1]][pos[0]]
    #print(f'get_next_pos({position}): {c}')
    dirs=[]
    if (c,dir) not in next_dirs:
        dirs.append(dir)
    else:
        dirs.extend(next_dirs[(c,dir)])
    result = []
    for d in dirs:
        p = (pos[0]+d[0], pos[1]+d[1])
        #print(p, d)
        if (pos_in_grid(p)):
            result.append((p,d))
    #print(f'{result}')
    return result


def count_energized(posdir):
    energized = set()
    visited = set()
    stack = [posdir]
    while len(stack)>0:
        posdir = stack.pop(0)
        energized.add(posdir[0])
        visited.add(posdir)
        for p in get_next_pos(posdir):
            if p not in visited:
                stack.append(p)
    return len(energized)

#part one:
print(count_energized(((0,0), (1,0))))

#part two
e = []
for x in range(max_x+1):
    e.append(count_energized(((x,0), (0,1))))
    e.append(count_energized(((x,max_y), (0,-1))))
for y in range(max_y+1):
    e.append(count_energized(((0,y), (1,0))))
    e.append(count_energized(((max_x,y), (-1,0,))))

print(max(e))