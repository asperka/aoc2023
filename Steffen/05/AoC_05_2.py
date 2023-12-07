# -*- coding: utf-8 -*-

import re

def execute():
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

    class Range:
        def __init__(self, target, source, nr):
            self.target = target
            self.source = source
            self.nr = nr

        def __str__(self):
            return f'Range(target: {self.target}, source: {self.source}, nr: {self.nr})'

        def __repr__(self):
            return f'Range(target: {self.target}, source: {self.source}, nr: {self.nr})'

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
                map['ranges'].append( Range(nrs[0], nrs[1], nrs[2]))

    #print (maps)
    seedranges = []
    for i in range(0, len(seeds), 2):
        seedranges.append(range(seeds[i], seeds[i]+seeds[i+1]))
    #print (seedranges)

    def map_range(value_range, mapping):
        ##print (value_range[-1], mapping.source)
        if value_range[-1] < mapping.source:
             return ([value_range], [])
        #print (value_range[0], mapping.source+ mapping.nr - 1)
        if value_range[0] > mapping.source + mapping.nr - 1:
            return ([value_range], [])
        unmapped = []
        if (value_range[0] < mapping.source):
            unmapped.append(range(value_range[0], mapping.source))
            value_range = range(mapping.source, value_range[-1]+1)
        #print (value_range[-1] , mapping.source + mapping.nr - 1)
        if (value_range[-1] > mapping.source + mapping.nr - 1):
            unmapped.append(range(mapping.source + mapping.nr, value_range[-1]+1))
            value_range = range(value_range[0], mapping.source + mapping.nr)
        
        offset = value_range[0]-mapping.source
        return (unmapped, [range(mapping.target + offset, mapping.target + offset + len(value_range))])

    target = 'seed'
    unmapped = seedranges
    while True:
        #print (maps[target])
        u2 = []
        mapped = []
        for mapping in maps[target]['ranges']:
            #print (unmapped)
            for v in unmapped:
                (r,m) = map_range(v, mapping)
                #print (v, mapping, '->', r, m)
                u2.extend(r)
                mapped.extend(m)
            unmapped = u2
            u2 = []
        unmapped.extend(mapped)
        #print (target, seedranges, maps[target]['ranges'], "->", unmapped)
        target = maps[target]['target']
        if not target in maps:
            break

    print(min([r[0] for r in unmapped]))

import timeit
print (timeit.timeit('execute()', number=1000, globals=globals()))