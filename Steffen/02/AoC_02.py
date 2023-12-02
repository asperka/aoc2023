# -*- coding: utf-8 -*-

import re

text="""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
text = open("input.txt").read()

lines = filter(None, text.split('\n'))
games_max_nr = {}
for l in lines:
    m = re.match('Game (\d*): (.*)', l)
    #print (l, m)
    id = int(m.group(1))
    games = m.group(2).split(';')
    max_nr = {'red': 0, 'blue': 0, 'green': 0}
    for g in games:
        #print (g)
        colours = g.split(',')
        for col in colours:
            nr, c = col.split()
            nr = int(nr)
            if max_nr[c] < nr:
                max_nr[c] = nr
    games_max_nr[id] = max_nr

ids = []
max = {'red': 12, 'green': 13, 'blue': 14}
for id in games_max_nr:
    colours = games_max_nr[id]
    possible = True
    for c in max:
        if colours[c] > max[c]:
            possible = False
    if possible:
        ids.append(id)

print (games_max_nr)
print (sum(ids))