# -*- coding: utf-8 -*-

import re
import numpy as np

text="""\
Time:      7  15   30
Distance:  9  40  200
"""
#text = open("input.txt").read()

lines = text.split('\n')

CARDS = 'J23456789TQKA'
RANKS = ['HIGH_FIVE', 'ONE_PAIR', 'TWO_PAIR', 'THREE_OF_A_KIND', 'FULL_HOUSE', 'FOUR_OF_A_KIND', 'FIVE_OF_A_KIND']

def cmp_card(a, b):
    if a==b:
        return 0
    res = CARDS.find(a) - CARDS.find(b)
    return int(res/abs(res))


def test_card_eq():
    assert(cmp_card('T','T')==0)

def test_card_lt():
    assert(cmp_card('7','T')==-1)
    
def test_card_gt():
    assert(cmp_card('T','7')==1)

#----------

def calc_basic_rank(cards):
    nrs = {}
    diff_cards = set()
    for c in CARDS:
        nrs[c] = 0
    for c in cards:
        nrs[c] += 1
        diff_cards.add(c)
    if (len(diff_cards) == 5):
        return 'HIGH_FIVE'
    if (len(diff_cards) == 4):
        return 'ONE_PAIR'
    if (len(diff_cards) == 3 and max(nrs.values())==2):
        return 'TWO_PAIR'
    if (len(diff_cards) == 3 and max(nrs.values())==3):
        return 'THREE_OF_A_KIND'
    if (len(diff_cards) == 2 and max(nrs.values())==3):
        return 'FULL_HOUSE'
    if ( max(nrs.values())==4):
        return 'FOUR_OF_A_KIND'
    if ( max(nrs.values())==5):
        return 'FIVE_OF_A_KIND'
    return ''

def calc_rank(cards):
    ranki = RANKS.index(calc_basic_rank(cards))
    for r in CARDS:
        c = cards.replace('J', r)
        r = calc_basic_rank(c)
        ri = RANKS.index(r)
        ranki = max([ranki, ri])
    return RANKS[ranki]

def test_rank_high_five():
    assert(calc_rank('2345A') == 'HIGH_FIVE')
    
def test_rank_one_pair():
    assert(calc_rank('A23A4') == 'ONE_PAIR')

def test_rank_two_pair():
    assert(calc_rank('23432') == 'TWO_PAIR')

def test_rank_three_of_a_kind():
    assert(calc_rank('TTT98') == 'THREE_OF_A_KIND')
    
def test_rank_full_house():
    assert(calc_rank('23332') == 'FULL_HOUSE')

def test_rank_four_of_a_kind():
    assert(calc_rank('AA8AA') == 'FOUR_OF_A_KIND')
    
def test_rank_five_of_a_kind():
    assert(calc_rank('AAAAA') == 'FIVE_OF_A_KIND')

def test_rank_four_of_a_kind_joker():
    assert(calc_rank('QJJQ2') == 'FOUR_OF_A_KIND')


#--------

def cmp_cards(a, b):
    if a == b:
        return 0
    rank_a = RANKS.index(calc_rank(a))
    rank_b = RANKS.index(calc_rank(b))
    if rank_a > rank_b:
        return 1
    if rank_a < rank_b:
        return -1
    for i in range(5):
        c = cmp_card(a[i], b[i])
        if c != 0:
            return c
    return 0

def test_cards_eq():
    assert(cmp_cards('AAABB', 'AAABB') == 0)

def test_cards_higher_rank():
    assert(cmp_cards('AAAAA', '23432') == 1)

def test_cards_lower_rank():
    assert(cmp_cards('23456', '23432') == -1)

def test_cards_stronger():
    assert(cmp_cards('33332', '2AAAA') == 1)

def test_cards_stronger2():
    assert(cmp_cards('QQQQ2', 'JKKK2') == 1)

def test_cards_weaker():
    assert(cmp_cards('77788', '77888') == -1)

#------------
import functools

def sort_cards(cards):
    return sorted(cards, key=functools.cmp_to_key(cmp_cards))

def test_sorting():
    cards = ['32T3K', 'T55J5', 'KK677', 'KTJJT', 'QQQJA']
    assert(sort_cards(cards) == ['32T3K', 'KK677', 'T55J5', 'QQQJA',  'KTJJT'] )

#-----------
text = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

def create_cards(cards):
    lines = cards.split('\n')
    lines = filter(None,lines)
    result = {}
    for l in lines:
        t = l.split(' ')
        result[t[0]] = int(t[1])
    return result

def test_create_cards():
    assert(create_cards(text) == 
           {'32T3K': 765, 'T55J5': 684, 'KK677': 28,'KTJJT': 220,'QQQJA': 483})

def calc_winning(cards_text):
    cards = create_cards(cards_text)
    sorted_keys = sort_cards(cards.keys())
    results = [(i+1)*cards[k] for (i, k) in enumerate(sorted_keys)]
    return sum(results)

def test_calc_winning():
    assert(calc_winning(text) == 5905)

text = open("input.txt").read()
print(calc_winning(text))
