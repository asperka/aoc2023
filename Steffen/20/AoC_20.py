# -*- coding: utf-8 -*-

import re

text="""
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""
text="""
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

text = open("input.txt").read()

HIGH = 1
LOW = 0

OFF = 0
ON = 1

pulses = []

class Module:
    def __init__(self, name):
        self.name = name
        self.outputs = []
        self.last_pulse = HIGH
    def add_input(self, i):
        ...
    def add_output(self, o):
        self.outputs.append(o)
    def Receive(self, input, pulse):
        self.last_pulse = pulse
    def __repr__(self):
        return f'{self.__class__.__name__}: outputs: {[o.name for o in self.outputs]}'

class Broadcaster(Module):
    def __init__(self, name):
        super().__init__(name)
    def Receive(self, input, pulse):
        for m in self.outputs:
            pulses.append((m, self, pulse))

class Output(Module):
    def __init__(self, name):
        super().__init__(name)
        self.received = []
    def Receive(self, input, pulse):
        self.received.append(pulse)
            
class FlipFlop(Module):
    def __init__(self, name):
        super().__init__(name)
        self._state = OFF
    def Receive(self, input, pulse):
        if pulse == HIGH:
            return
        output = LOW
        if self._state == OFF:
            self._state = ON
            output = HIGH
        else:
            self._state = OFF
            output = LOW
        for m in self.outputs:
            pulses.append((m, self, output))
            
class Conjunction(Module):
    def __init__(self, name):
        super().__init__(name)
        self.input_states = {}
    def add_input(self, i):
        self.input_states[i] = LOW
    def Receive(self, input, pulse):
        self.input_states[input] = pulse
        if LOW in self.input_states.values():
            output = HIGH
        else:
            output = LOW
        for m in self.outputs:
            pulses.append((m, self, output))
    def __repr__(self):
        return f'{self.__class__.__name__}: inputs: {[m.name for m,s in self.input_states.items()]}, outputs: {[o.name for o in self.outputs]}'
            
def create_module(text):
    typename, _ = text.split(' -> ')
    if typename[0] == '%':
        return FlipFlop(typename[1:])
    elif typename[0] == '&':
        return Conjunction(typename[1:])
    else:
        return Broadcaster(typename)
       
    

modules = {}
for line in filter(None, text.split('\n')):
    m = create_module(line)
    modules[m.name] = m

for line in filter(None, text.split('\n')):
    name, outputs = line.split(' -> ')
    if name[0] == '%' or name[0] == '&':
        name = name[1:]
    m = modules[name]
    for o in outputs.split(', '):
        if o not in modules:
            modules[o] = Module(o)
        m.outputs.append(modules[o])
        modules[o].add_input(m)

#print(modules)
button = Module('Button')
count = {LOW:0, HIGH:0}
for run in range(1000):
    pulses.append((modules['broadcaster'], button, LOW))
    while len(pulses) > 0:
        (m, i, p) = pulses.pop(0)
        count[p] += 1
        m.Receive(i,p)

print (count, count[LOW] * count[HIGH])