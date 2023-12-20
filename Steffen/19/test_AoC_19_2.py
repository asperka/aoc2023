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

def parse_lines(lines):
    rules = {}
    idx = 0
    while lines[idx] == '':
        idx+=1
    while lines[idx] != '':
        name, conditions = parse_rule(lines[idx])
        rules[name] = conditions
        idx+=1
    return rules

def execute_condition(part, condition):
    if condition.find(':') < 0:
        return (part, condition), None
    m = re.match('([xmas])(.)(-?\d+):(\w+)', condition)
    cat = m.group(1)
    op = m.group(2)
    value = int(m.group(3))
    workflow = m.group(4)
    if op == '<':
        if part[cat][0] >= value:
            return (None, None), part
        if part[cat][1] < value:
            return (part, workflow), None
        p1 = part.copy()
        p1[cat] = (p1[cat][0], value-1)
        p2 = part.copy()
        p2[cat] = (value, p2[cat][1])
        return (p1, workflow), p2
    elif op == '>':
        if part[cat][1] <= value:
            return (None, None), part
        if part[cat][0] > value:
            return (part, workflow), None
        p1 = part.copy()
        p1[cat] = (value+1, p1[cat][1])
        p2 = part.copy()
        p2[cat] = (p2[cat][0], value)
        return (p1, workflow), p2
    return None 



def test_execute_condition_no_operation():
    p = {'x':(1,100)}
    cond = 'abc'
    assert(execute_condition(p, cond) == ((p, cond), None))

def test_execute_condition_gt_no_workflow():
    p = {'x':(1,40)}
    cond = 'x>200:abc'
    assert(execute_condition(p, cond) == ((None, None), {'x':(1,40)}))

def test_execute_condition_gt_no_split():
    p = {'x':(1,40)}
    cond = 'x<200:abc'
    assert(execute_condition(p, cond) == (({'x':(1,40)}, 'abc'), None))

def test_execute_condition_gt_split():
    p = {'x':(1,400)}
    cond = 'x<200:abc'
    assert(execute_condition(p, cond) == (({'x':(1,199)}, 'abc'), {'x':(200,400)}))

def test_execute_condition_lt_split():
    p = {'x':(1,400)}
    cond = 'x>200:abc'
    assert(execute_condition(p, cond) == (({'x':(201,400)}, 'abc'), {'x':(1,200)}))

def test_execute_condition_lt_no_split():
    p = {'x':(1000,2400)}
    cond = 'x>200:abc'
    assert(execute_condition(p, cond) == (({'x':(1000,2400)}, 'abc'), None))

def test_execute_condition_lt_no_workflow():
    p = {'x':(1000,2400)}
    cond = 'x<200:abc'
    assert(execute_condition(p, cond) == ((None, None), {'x':(1000,2400)}))

def test_parse_lines():
    text="""\
    px{a<2006:qkq,m>2090:A,rfg}
    pv{a>1716:R,A}

    {x=787,m=2655,a=1222,s=2876}
    {x=2127,m=1623,a=2188,s=1013}"""
    lines = text.split('\n')
    rules = parse_lines(lines)
    assert(rules == {'px':['a<2006:qkq','m>2090:A','rfg'],
                     'pv':['a>1716:R','A']})


def execute_conditions(part, conditions):
    resolved = []
    accepted = []
    for c in conditions:
        if part is not None:
            res, part = execute_condition(part, c)
            if res[1] is not None:
                if res[1] == 'A':
                    accepted.append(res[0])
                elif  res[1] != 'R':
                    resolved.append(res)
    print (resolved, accepted)
    return resolved, accepted


def test_execute_condtions_1():
    p = {'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(1,4000)}
    cs = ['s>2770:qs','m<1801:hdj','R']
    assert( execute_conditions(p, cs) == (
        [({'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(2771,4000)}, 'qs'),
         ({'x':(1,4000),'m':(1,1800),'a':(1,4000),'s':(1,2770)}, 'hdj')],
        []
    ))

def test_execute_condtions_2():
    p = {'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(1,4000)}
    cs = ['s<537:gd','x>2440:R','A']
    assert( execute_conditions(p, cs) == (
        [({'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(1,536)}, 'gd')],
        [{'x':(1,2440),'m':(1,4000),'a':(1,4000),'s':(537,4000)}]
    ))

def test_parse_rule():
    assert(parse_rule('qqz{s>2770:qs,m<1801:hdj,R}') == 
           ('qqz', ['s>2770:qs', 'm<1801:hdj', 'R']))

