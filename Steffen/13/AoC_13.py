# -*- coding: utf-8 -*-

text = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.


#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

text = """\
#####....####
..##..##..##.
###..#..#..##
##..##..##..#
##..#....#..#
###...#....##
..###.##.###.
####.####.###
..##.####.##.
###.##..##.##
##...#..#...#
"""

text = open("input.txt").read()

def create_columns(rows):
    columns = [[] for _ in range(len(rows[0]))]
    for r in rows:
        for i, c in enumerate(r):
            columns[i].append(c)
    return columns

def find_reflection(rows, old_solution=-1):
    for row in range(0, len(rows) - 1):
        if rows[row] == rows[row + 1]:
            r = 1
            reflection = True
            while row - r >= 0 and row + r + 1 < len(rows):
                if rows[row - r] != rows[row + r + 1]:
                    reflection = False
                r += 1
            if reflection and (row + 1) != old_solution:
                return row + 1
    return 0

def search_reflection(rows, old_solution):
    for r, c in [
        (r, c)
        for r in range(len(rows))
        for c in range(len(rows[0]))
        if rows[r][c] == "."
    ]:
        rows[r][c] = "#"
        result = find_reflection(rows, old_solution)
        rows[r][c] = "."
        if result != 0:
            return result
    return 0


def search_reflections(rows, old_solution):
    nr = search_reflection(rows, old_solution[0])
    if nr > 0:
        return (nr, 0)
    else:
        return (0, search_reflection(create_columns(rows), old_solution[1]))

def find_reflections(rows):
    nr = find_reflection(rows)
    if nr > 0:
        return (nr, 0)
    else:
        return (0, find_reflection(create_columns(rows)))

def print_grid(grid):
    for line in grid:
        print(" ".join(line))
    print()

nr_row_reflections = 0
nr_col_reflections = 0
nr_row_reflections2 = 0
nr_col_reflections2 = 0

rows = []
for line in [list(t) for t in text.split("\n")]:
    if len(line) > 0:
        rows.append(line)
    elif len(rows) > 0:
        (r, c) = find_reflections(rows)
        nr_row_reflections += r
        nr_col_reflections += c
        (r2, c2) = search_reflections(rows, (r, c))
        nr_row_reflections2 += r2
        nr_col_reflections2 += c2
        rows = []

print('Part One:')
print("rows", nr_row_reflections)
print("cols", nr_col_reflections)
print(nr_row_reflections * 100 + nr_col_reflections)
print()
print('Part Two:')
print("rows", nr_row_reflections2)
print("cols", nr_col_reflections2)
print(nr_row_reflections2 * 100 + nr_col_reflections2)
