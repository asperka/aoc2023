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

rocks = text.split('\n')
rocks = list(filter(None, rocks))

def print_rocks(rocks):
    for r in rocks:
        print(''.join(r))
    print()

def rotate_right(lines):
    rocks = []
    for x in range (len(lines[0])):
        str = ''
        for y in range(len(lines)):
            str += lines[-(y+1)][x]
        rocks.append(str)
    return rocks

def rotate_left(lines):
    rocks = []
    for x in range (len(lines[0])):
        str = ''
        for y in range(len(lines)):
            str += lines[y][-(x+1)]
        rocks.append(str)
    return rocks

def roll(lines):
    rocks = []
    for str in lines:
        while str.find('.O') > -1:
            str = str.replace('.O', 'O.')
        rocks.append(str)
    return rocks

def calc_load(rocks):
    factor = len(rocks)
    load = 0
    for r in rocks:
        load += r.count('O')*factor
        factor -= 1
    return load

cycle = 0
loads = []
for _ in range(1000):
    rocks = rotate_left(rocks)
    rocks = roll(rocks)
    for _ in range(3):
        rocks = rotate_right(rocks)
        rocks = roll(rocks)
    rocks = rotate_right(rocks)
    rocks = rotate_right(rocks)
    loads.append(calc_load(rocks))
print(loads)