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

text = open("input.txt").read()

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


def execute_conditions(part, conditions):
    resolved = []
    accepted = []
    for c in conditions:
        if part is not None:
            res, part = execute_condition(part, c)
            if res[1] is not None:
                if res[1] == 'A':
                    accepted.append(res[0])
                elif res[1] != 'R':
                    resolved.append(res)
    return resolved, accepted

rules = parse_lines(lines)

parts = [({'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(1,4000)}, 'in')]
accepted = []
while len(parts)>0:
    p = parts.pop(0)
    res, ac = execute_conditions(p[0], rules[p[1]])
    accepted.extend(ac)
    parts.extend(res)

#print(accepted)
sum = 0
for a in accepted:
    s = 1
    for v1, v2 in a.values():
        s *= v2-v1+1
    sum+=s
print(sum)