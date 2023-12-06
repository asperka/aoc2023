# -*- coding: utf-8 -*-

import re
import numpy as np

text="""\
Time:      7  15   30
Distance:  9  40  200
"""
text = open("input.txt").read()

lines = text.split('\n')
times = [int(x) for x in re.findall('\d+', lines[0])]
dist = [int(x) for x in re.findall('\d+', lines[1])]

def calc_dist(acc, time):
    return acc*(time-acc)

wins = np.array([0]*len(times))
for race in range(len(times)):
    for t in range(times[race]):
        if calc_dist(t, times[race]) > dist[race]:
            wins[race]+=1
print(times, dist)
print(wins)
print(wins.prod())