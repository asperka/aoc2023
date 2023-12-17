# -*- coding: utf-8 -*-

import re

text="""\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
text = open("input.txt").read()

lines = list(filter(None, text.split('\n')))

nrs = [[int(n) for n in re.findall('-?\d+', l)] for l in lines]

def diff(nrs):
    result = []
    for i in range(len(nrs)-1):
        result.append((nrs[i+1]-nrs[i]))
    return result

def calc_diffs(nrs):
    diffs = [nrs]
    while True:
        d = diff(diffs[-1])
        diffs.append(d)
        all_zero = True
        for n in d:
            if n != 0:
                all_zero = False
        if all_zero:
            return diffs

def extend_arrays(d):
    i = len(d)-1
    while i>0:
        d[i-1].append(d[i-1][-1]+d[i][-1])
        i-=1

result = []
for n in nrs:
    n.reverse()
    d = calc_diffs(n)
    extend_arrays(d)
    result.append(int(d[0][-1]))

print (sum(result))