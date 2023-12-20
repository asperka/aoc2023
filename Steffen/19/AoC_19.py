# -*- coding: utf-8 -*-

# 19.12. 6:59
import re

text = """\
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

lines = text.split("\n")


def parse_rule(text):
    m = re.match("(\w+){(.*)}", text.strip())
    name = m.group(1)
    conditions = m.group(2).split(",")
    return name, conditions


def create_part_from_text(text):
    text = text.strip()[1:-1]
    pairs = (v.split("=") for v in text.split(","))
    return {k: int(n) for (k, n) in pairs}


def parse_lines(lines):
    rules = {}
    parts = []
    idx = 0
    while lines[idx] == "":
        idx += 1
    while lines[idx] != "":
        name, conditions = parse_rule(lines[idx])
        rules[name] = conditions
        idx += 1
    idx += 1
    while idx < len(lines):
        if lines[idx] != "":
            parts.append(create_part_from_text(lines[idx]))
        idx += 1
    return rules, parts


def execute_condition(part, condition):
    if condition.find(":") < 0:
        return condition
    m = re.match("([xmas])(.)(-?\d+):(\w+)", condition)
    cat = m.group(1)
    op = m.group(2)
    value = int(m.group(3))
    workflow = m.group(4)
    if op == "<":
        if part[cat] < value:
            return workflow
    elif op == ">":
        if part[cat] > value:
            return workflow
    return None


def execute_conditions(part, conditions):
    for c in conditions:
        r = execute_condition(part, c)
        if r is not None:
            return r


def execute_rules(part, rules):
    conditions = rules["in"]
    while True:
        rule = execute_conditions(part, conditions)
        if rule == "A" or rule == "R":
            return rule
        conditions = rules[rule]


rules, parts = parse_lines(lines)
print(
    sum(
        sum(p.values())
        for p in parts if execute_rules(p, rules) == "A"
    )
)
