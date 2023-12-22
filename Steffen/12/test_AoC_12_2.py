# -*- coding: utf-8 -*-

from functools import cache
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
    return tuple([len(g) for g in groups])

def split_line(line):
    l = line.split(' ')
    nrs = re.findall('\d+', l[1])
    return (l[0].strip('.'), tuple([int(n) for n in nrs]))

def split_line_2(line):
    l = line.split(' ')
    text = l[0]
    nrs = re.findall('\d+', l[1])
    for _ in range(4):
        text = text + '?' + l[0]
        nrs.extend(re.findall('\d+', l[1]))
    return (text, tuple([int(n) for n in nrs]))

def test_count_damaged():
    assert(count_damaged('.#...#....###.')==(1,1,3))
    
def test_split():
    assert(split_line('.??..??...?##. 1,2,3')==('??..??...?##', (1,2,3)))

def long_enough(text, groups):
    return sum(groups)+len(groups)-1 <= len(text)

def test_long_enough():
    assert(long_enough('?????', (1,))==True)
    assert(long_enough('?????', (1,3))==True)
    assert(long_enough('????', (2,1))==True)
    assert(long_enough('?????', (2,3))==False)

def first_group_too_long(text, nr):
    idx = 0
    while text[idx]=='#' and (len(text)-1)>idx:
        idx+=1
    return idx>nr
    
def test_first_group_too_long():
    assert(first_group_too_long('#???', 1)==False)
    assert(first_group_too_long('#??', 2)==False)
    assert(first_group_too_long('##?', 2)==False)
    assert(first_group_too_long('###', 4)==False)
    assert(first_group_too_long('###?', 2)==True)

@cache
def count_sln(text, groups):
    text = text.strip('.')
    if not long_enough(text, groups):
        return 0
    if len(groups)==0:
        if '#' in text:
            return 0
        return 1
    if first_group_too_long(text, groups[0]):
        return 0
    if '.' not in text and '?' not in text:
        if len(groups) == 1:
            if len(text) == groups[0]:
                return 1
            return 0
    if '?' not in text:
        if (count_damaged(text)) == groups:
            return 1
        return 0
    p = text.find('?')
    if p>0:
        start = text[:p]
        p = start.rfind('.')
        if (p>0):
            groups_before_first_q = start[:p]
            cnt = count_damaged(groups_before_first_q)
            if groups[:len(cnt)] != cnt:
                return 0
            text = text[p:]
            groups = groups[len(cnt):]
            if len(groups)==0 and '#' in text:
                return 0
    result = count_sln(text.replace('?', '.', 1), groups) + count_sln(text.replace('?', '#', 1), groups)
    return result

def test_count_sln_one_left1():
    assert(count_sln('...###', (3,)) == 1)

def test_count_sln_one_left2():
    assert(count_sln('...##', (2,)) == 1)

def test_count_sln_one_left3():
    assert(count_sln('...###',(2,)) == 0)

def test_count_sln_one_left4():
    assert(count_sln('...###', (3, 1)) == 0)

def test_count_sln_one_left5():
    assert(count_sln('###', (3,)) == 1)

def test_count_sln_one_left6():
    assert(count_sln('#?#', (3,)) == 1)

def test_count_sln_one_left7():
    assert(count_sln('..???', (3,)) == 1)

def test_count_sln_no_unknown_left1():
    assert(count_sln('...#...##', (1, 2)) == 1)

def test_count_sln_no_unknown_left2():
    assert(count_sln('.#.#...##', (1, 2)) == 0)

def test_count_sln_one_replacment_left2():
    assert(count_sln('.#?#...##', (3, 2)) == 1)
           
def test_count_sln_two_replacments_left1():
    assert(count_sln('.?##?...##', (3, 2)) == 2)

def test_count_sln_test_1():
    assert(count_sln('??#??##??###', (1, 2, 3)) == 1)

def test_count_sln_test_2():
    assert(count_sln('#?', (1,)) == 1)

def test_count_sln_examples_part1_1():
    assert(count_sln('???.###', ( 1,1,3 )) == 1 )
    assert(count_sln('.??..??...?##.', ( 1,1,3 )) == 4 )
    assert(count_sln('?#?#?#?#?#?#?#?', ( 1,3,1,6 )) == 1 )
    assert(count_sln('????.#...#...', ( 4,1,1 )) == 1 )
    assert(count_sln('????.######..#####.', ( 1,6,5 )) == 4 )
    assert(count_sln('?###????????', ( 3,2,1 )) == 10 )

def test_split_line_2():
    assert(split_line_2('???.### 1,1,3') 
           == ('???.###????.###????.###????.###????.###', (1,1,3,1,1,3,1,1,3,1,1,3,1,1,3)))

def test_count_sln_examples_part2_1():
    assert(count_sln(*split_line_2('???.### 1,1,3')) == 1)

def test_count_sln_examples_part2_2():
    assert(count_sln(*split_line_2('.??..??...?##. 1,1,3')) == 16384 )
    assert(count_sln(*split_line_2('?#?#?#?#?#?#?#? 1,3,1,6')) == 1 )
    assert(count_sln(*split_line_2('????.#...#... 4,1,1')) == 16 )
    assert(count_sln(*split_line_2('????.######..#####. 1,6,5')) == 2500)
    assert(count_sln(*split_line_2('?###???????? 3,2,1')) == 506250 )

print(sum([count_sln(*split_line_2(l)) for l in lines]))