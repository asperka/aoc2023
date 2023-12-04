# -*- coding: utf-8 -*-
import regex

text="""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
text = open("input.txt").read()

nrs = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6': '6', '7': '7', '8':'8', '9':'9', 
       'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six': '6', 'seven': '7', 'eight':'8', 'nine':'9'}
lines = text.split()
sum = 0
for l in lines:
    m = regex.findall('[1-9]|one|two|three|four|five|six|seven|eight|nine', l, overlapped = True)
    nr = nrs[m[0]]+nrs[m[-1]]
    sum += int(nr)
print (sum)