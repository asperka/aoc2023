# -*- coding: utf-8 -*-

import re

text="""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
text = open("input.txt").read()

lines = text.split('\n')

maps = {}
seeds = []
source = ''
target = ''
map = {}
for l in lines:
    if len(l) == 0 and source != '':
        maps[source] = map
        map = {}
    if l.startswith('seeds:'):
        seeds = [int(s) for s in re.findall('\d+', l)]
    else:
        m = re.match('([\w]+)-to-([\w]+) map:', l)
        if m:
            source = m.group(1)
            target = m.group(2)
            map['target']=target
            map['ranges'] = []
        elif len(l)>0:
            nrs = [int(n) for n in re.findall('\d+', l)]
            map['ranges'].append( 
                (range(nrs[0], nrs[0]+nrs[2]),range(nrs[1], nrs[1]+nrs[2])
                 ))

locations = []
for s in seeds:
    source = 'seed'
    value = s
    while source != 'location':
        m = maps[source]
        #print (source, value)
        for (t, s) in m['ranges']:
             if value in s:
                 #print (t, s)
                 d = value-s[0]
                 value = t[0]+d
                 break
        source = m['target']
    locations.append(value)
        
print (locations)
print (min(locations))