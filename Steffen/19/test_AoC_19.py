# -*- coding: utf-8 -*-

# 19.12. 6:59
import re

text="""\
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

#text = open("input.txt").read()

lines = text.split('\n')

def parse_rule(text):
    print('R', text)
    m = re.match('(\w+){(.*)}', text.strip())
    name = m.group(1)
    conditions = m.group(2).split(',')
    return name, conditions

def create_part_from_text(text):
    text = text.strip()[1:-1]
    pairs = (v.split('=') for v in text.split(','))
    return {k:int(n) for (k,n) in pairs}

def parse_lines(lines):
    rules = {}
    parts = []
    idx = 0
    while lines[idx] == '':
        idx+=1
    while lines[idx] != '':
        name, conditions = parse_rule(lines[idx])
        rules[name] = conditions
        idx+=1
    idx+=1
    while idx<len(lines):
        parts.append(create_part_from_text(lines[idx]))
        idx+=1
    return rules, parts

def execute_condition(part, condition):
    if condition.find(':') < 0:
        return condition
    m = re.match('([xmas])(.)(-?\d+):(\w+)', condition)
    cat = m.group(1)
    op = m.group(2)
    value = int(m.group(3))
    workflow = m.group(4)
    if op == '<':
        if part[cat] < value:
            return workflow 
    elif op == '>':
        if part[cat] > value:
            return workflow
    return None 

def execute_conditions(part, conditions):
    for c in conditions:
        r = execute_condition(part, c)
        if r is not None:
            return r

def test_parse_rule():
    assert(parse_rule('qqz{s>2770:qs,m<1801:hdj,R}') == 
           ('qqz', ['s>2770:qs', 'm<1801:hdj', 'R']))

def test_create_part():
    p = create_part_from_text('{x=787,m=2655,a=1222,s=2876}')
    assert(p['x'] == 787 and p['m'] == 2655 and p['a']==1222 and p['s'] == 2876)

def test_execute_condition_gt_failed():
    p = {'x':100}
    cond = 'x>200:abc'
    assert(execute_condition(p, cond) is None)

def test_execute_condition_no_operation():
    p = {'x':100}
    cond = 'R'
    assert(execute_condition(p, cond) == 'R')

def test_execute_condition_gt():
    p = {'x':300}
    cond = 'x>200:abc'
    assert(execute_condition(p, cond) == 'abc')

def test_execute_condition_lt():
    p = {'x':500, 'm':200}
    cond = 'm<400:abc'
    assert(execute_condition(p, cond) == 'abc')

def test_parse_lines():
    text="""\
    px{a<2006:qkq,m>2090:A,rfg}
    pv{a>1716:R,A}

    {x=787,m=2655,a=1222,s=2876}
    {x=2127,m=1623,a=2188,s=1013}"""
    lines = text.split('\n')
    rules, parts = parse_lines(lines)
    print (parts)
    assert(rules == {'px':['a<2006:qkq','m>2090:A','rfg'],
                     'pv':['a>1716:R','A']})
    assert(parts == [{'a':1222,'m':2655,'s':2876,'x':787},
                     {'a':2188,'m':1623,'s':1013,'x':2127}])

def test_execute_condtions_1():
    p = {'x':787,'m':2655,'a':1222,'s':2876}
    cs = ['s>2770:qs','m<1801:hdj','R']
    assert( execute_conditions(p, cs) == 'qs')

def test_execute_condtions_2():
    p = {'x':2127,'m':1623,'a':2188,'s':1013}
    cs = ['s<537:gd','x>2440:R','A']
    assert( execute_conditions(p, cs) == 'A')

