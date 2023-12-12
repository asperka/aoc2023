# -*- coding: utf-8 -*-

import itertools

text="""\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
text = open("input.txt").read()
lines = list(filter(None, text.split('\n')))

# Part One
factor = 2

# Part Two
#factor = 1000000


empty_lines = [i for (i,l) in enumerate(lines) if l.count('#') == 0]

def count_galaxies(row):
    return sum([1 for l in lines if l[row]=='#'])

empty_rows = [r for r in range(len(lines[0])) if count_galaxies(r) == 0]

galaxies = [(x,y) for (x,y) in itertools.product(range(len(lines[0])), range(len(lines))) if lines[y][x] == '#']

def calc_dist(g1, g2):
    (x1, y1) = galaxies[g1]
    (x2, y2) = galaxies[g2]
    dist = abs(x2-x1) + abs(y2-y1)
    nrows = len([r for r in empty_rows if (r-x1)*(x2-r) > 0 ])
    nlines = len([l for l in empty_lines if (l-y1)*(y2-l) > 0])
    return dist + (factor-1) * (nrows + nlines)


pairs = itertools.combinations(range(len(galaxies)), 2)
sum = sum([calc_dist(g1, g2) for (g1, g2) in pairs])
print(sum)