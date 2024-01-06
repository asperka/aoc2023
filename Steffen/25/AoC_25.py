# -*- coding: utf-8 -*-

import networkx as nx

text="""
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""
text = open("input.txt").read()

lines = text.split('\n')
lines = list(filter(None, lines))

def add_node(nodes, node):
    if node not in nodes:
        nodes[node] = set()

G = nx.Graph()
nodes = {}
for line in lines:
    node, children = line.split(':')
    add_node(nodes, node)
    for child in children.split():
        add_node(nodes, child)
        nodes[node].add(child)
        nodes[child].add(node)
        G.add_edge(node, child)
    
#print (nodes)
communities = nx.algorithms.community.girvan_newman(G)
for c in communities:
    if len(c) == 2:
        print(len(c[0]), len(c[1]), len(c[0])*len(c[1]))