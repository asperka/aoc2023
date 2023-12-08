# -*- coding: utf-8 -*-

class Range:
        def __init__(self, target, source, nr):
            self.target = target
            self.source = source
            self.nr = nr

        def __str__(self):
            return f'Range(target: {self.target}, source: {self.source}, nr: {self.nr})'

        def __repr__(self):
            return f'Range(target: {self.target}, source: {self.source}, nr: {self.nr})'

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

def test_range1():
    assert (map_range(range(10,20), Range(100, 20, 10)) == ([range(10,20)], []))
def test_range2():
    assert (map_range(range(10,20), Range(30, 1, 9)) == ([range(10,20)], []))
def test_range3():
    assert (map_range(range(10,20), Range(30, 5, 20)) == ([], [range(35,45)]))
def test_range4():
    assert (map_range(range(10,20), Range(30, 15, 20)) == ([range(10,15)], [range(30,35)]))
def test_range5():
    assert (map_range(range(10,20), Range(30, 5, 10)) == ([range(15,20)], [range(35,40)]))
def test_range6():
    assert (map_range(range(10,20), Range(30, 15, 2)) == ([range(10, 15), range(17,20)], [range(30,32)]))
def test_range7():
    assert (map_range(range(11,18), Range(0, 1, 69)) == ([], [range(10,17)]))
def test_range8():
    assert (map_range(range(53,66), Range(0, 39, 15)) == ([range(54,66)], [range(14,15)]))

