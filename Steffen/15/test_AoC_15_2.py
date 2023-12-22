# -*- coding: utf-8 -*-

#22.12. 17:42

text="""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

text = open("input.txt").read()
codes = text[:-1].split(',')
codes = list(filter(None, codes))

def calcHASH(text):
    cv = 0
    for c in text:
        cv += ord(c)
        cv = (cv*17)%256
    return cv

def remove_lens(lens, boxes):
    box = calcHASH(lens)
    if box in boxes:
        boxes[box] = [(c,f) for (c,f) in boxes[box] if c != lens]

def test_remove_lens():
    boxes = {1:[('rn', 1), ('qp', 3), ('cm', 2)]}
    remove_lens('qp', boxes)
    assert(boxes == {1:[('rn', 1), ('cm', 2)]})
    remove_lens('qp', boxes)
    assert(boxes == {1:[('rn', 1), ('cm', 2)]})
    remove_lens('cm', boxes)
    assert(boxes == {1:[('rn', 1), ('cm', 2)]})

def add_lens(code, boxes):
    lens, f = code.split('=')
    box = calcHASH(lens)
    if box not in boxes:
        boxes[box] = []
    idx = -1
    for i in range(len(boxes[box])):
        if boxes[box][i][0] == lens:
            idx = i
    if idx >=0:
        boxes[box][idx] = (lens, int(f))
    else:
        boxes[box].append((lens, int(f)))

def test_add_lens():
    boxes = {}
    add_lens('rn=1', boxes)
    add_lens('qp=3', boxes)
    add_lens('cm=2', boxes)
    add_lens('rn=4', boxes)
    assert(boxes == {0:[('rn', 4), ('cm', 2)], 1:[('qp', 3)]})

boxes = {}
for c in codes:
    if '-' in c:
        remove_lens(c[:-1], boxes)
    else:
        add_lens(c, boxes)

#print(boxes)
sum = 0
for box, lenses in boxes.items():
    for i, lens in enumerate(lenses):
        sum += (box+1) * (i+1) * lens[1]

print(sum)