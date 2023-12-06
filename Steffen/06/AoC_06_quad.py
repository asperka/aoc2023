# -*- coding: utf-8 -*-

import re
import numpy as np
import math

text="""\
Time:      7  15   30
Distance:  9  40  200
"""
text = open("input.txt").read()

lines = text.split('\n')
times = [int(x) for x in re.findall('\d+', lines[0])]
dist = [int(x) for x in re.findall('\d+', lines[1])]

def solve(time, dist):
    t = time/2
    d = math.sqrt(t*t - dist)
    return (t-d, t+d)

wins = np.array([0]*len(times))
for race in range(len(times)):
    (t1,t2) = solve(times[race], dist[race])
    wins[race] = int(t2)-int(t1)
print(times, dist)
print(wins)
print(wins.prod())