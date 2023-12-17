# -*- coding: utf-8 -*-

import re

text="""\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
text = open("input.txt").read()
lines = list(filter(None, text.split('\n')))

def count_damaged(line):
    groups = [g for g in line.split('.') if g != '']
    return [len(g) for g in groups]

def replace(line, mask):
    nr = line.count('?')
    str = f'{mask:b}'
    str = str.zfill(nr)
    i = 0
    res = ''
    for c in line:
        if c == '?':
            if str[i] == '0':
                c = '.'
            else:
                c = '#'
            i+=1
        res += c
    return res

def split_line(line):
    l = line.split(' ')
    nrs = re.findall('\d+', l[1])
    return (l[0], [int(n) for n in nrs])

def count_possible(line):
    text, code = split_line(line)
    nr_q = text.count('?')
    nr = 2**nr_q
    #print (nr_q, nr, code)
    result = 0
    for n in range(nr):
        t = replace(text, n)
        c = count_damaged(t)
        #print(t, c)
        if c == code:
            result += 1
    return result

#for l in lines:
#    print(l, count_possible(l))

print(sum([count_possible(l) for l in lines]))