# -*- coding: utf-8 -*-

text = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

#text = open("input.txt").read()
blocks = [[int(c) for c in t] for t in text.split('\n') if t != '']
print (blocks)

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

class Crucible :
    def __init__(self):
        self.heat_loss = 0
        self.pos = (0,0)
        self.dir_idx = 0
        self.cnt_straigt = 3
    def clone(self):
        c = Crucible()
        c.heat_loss = self.heat_loss
        c.pos = self.pos
        c.dir_idx = self.dir_idx
        c.cnt_straigt = self.cnt_straigt
        return c
    def get_moves_possible(self):
        """return array with (direction indeces, step size)"""
        moves = []
        for i in [-1,0,1]:
            d = (self.dir_idx + i) % len(dirs)
            for s in range(1,4):
                if (self.test_dir(d, s)):
                    moves.append((d, s))
        return moves
    
    def test_dir(self, dir, steps):
        if self.dir_idx == dir and steps > self.cnt_straigt:
            return False
        x = self.pos[0] + dirs[dir][0]*steps
        y = self.pos[1] + dirs[dir][1]*steps
        return 0<=x<len(blocks[0]) and 0<=y<len(blocks)
    
    def move(self, dir, steps):
        self.pos = (self.pos[0] + dirs[dir][0]*steps, self.pos[1] + dirs[dir][1]*steps)
        if self.dir_idx == dir:
            self.cnt_straigt -= steps
        else:
            self.cnt_straigt = 3-steps
        self.dir_idx = dir
        self.heat_loss += blocks[self.pos[1]][self.pos[0]]
    
def test_moves_possibles():
    c = Crucible()
    assert(c.get_moves_possible() == [(0,1), (0,2), (0,3), (1,1), (1,2), (1,3)])

def test_moves_possibles1():
    c = Crucible()
    c.pos = (2,2)
    c.cnt_straigt = 1
    assert(c.get_moves_possible() == [(3,1), (3,2), (0, 1), (1,1), (1,2), (1,3)])

def test_moves_possibles2():
    c = Crucible()
    c.pos = (2,len(blocks)-1)
    assert(c.get_moves_possible() == [(3,1), (3,2), (1,1), (1,2), (1,3)])

def test_moves_possibles3():
    c = Crucible()
    c.pos = (2,2)
    c.cnt_straigt = 0
    assert(c.get_moves_possible() == [(3,1), (3,2), (1,1), (1,2), (1,3)])

###############
    
def test_move():
    c = Crucible()
    c.move(0, 1)
    assert(c.cnt_straigt == 2)
    assert(c.pos == (0,1))
    assert(c.heat_loss == blocks[1][0])

def test_move2():
    c = Crucible()
    c.move(1, 1)
    assert(c.cnt_straigt == 2)
    assert(c.pos == (1,0))
    assert(c.heat_loss == blocks[0][1])


