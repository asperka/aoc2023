# -*- coding: utf-8 -*-

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
import numpy as np

text = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
text = open("input.txt").read()

grammar = Grammar (
    r"""
    text = line+
    line = game_id colon ws games nl
    colon = ":"
    ws = ~"[\s]+"
    sp = " "
    nl = ~"\n"
    game_id     = word ws nr
    games       = (game semicolon)* game
    game        = (color comma)* color
    semicolon = "; "
    comma = ", "
    color = nr sp word
    word        = ~"\w+"
    nr          = ~"\d+"
    emptyline   = ws+
    """
    )
tree = grammar.parse(text)
# print ("----")
class Visitor(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.games = {}
        self.current_game = None
    def visit_text(self, node, visited_children):
        output = {}
        # print ('visit text...')
        for child in visited_children:
            output.update(child)
        return output

    def visit_line(self, node, visited_children):
        id, _, _, games, _ = visited_children
        # print(f'visit_line:return {id}: {games}')
        return {id: games}

    def visit_game_id(self, node, visited_children):
        _, _, id = visited_children
        # print (f'visit_game_id: return {id.text}')
        return id.text

    def visit_game(self, node, visited_children):
        result = {'red': 0, 'blue': 0, 'green': 0}
        children, last = visited_children
        result.update(last)
        for child in children:
            result.update(child[0])
        # print(f'visit_game: {result}')
        return result

    def visit_games(self, node, visited_children):
        result = []
        children, last = visited_children
        result.append(last)
        for child in children:
            result.append(child[0])
        # print(f'visit_games: {result}')
        return result
        
    def visit_color(self, node, visited_children):
        ## print(f'visit_color: {visited_children}')
        nr, _, col = visited_children
        result = {col.text: int(nr.text)};
        # print (f'visit_color: return {result}')
        return result

    def generic_visit(self, node, visited_children):
        ## print(f'generic_visit: {visited_children}')
        return visited_children or node


v = Visitor()
games = v.visit(tree)
print (len(games))

power = 0
for game in games.values():
    max_nr = {'red': 0, 'blue': 0, 'green': 0}
    for subset in game:
        for c, nr in subset.items():
            if max_nr[c] < nr:
                max_nr[c] = nr
    power += np.prod(list(max_nr.values()))

print (power)