#!/usr/bin/env python3

from common import read_input

data = read_input(10)

def parse_line(line):
    stack=[]
    value = {')':3,']':57,'}':1197,'>':25137}
    for c in line:
        if c == '<': stack.append('>')
        elif c == '(': stack.append(')')
        elif c == '[': stack.append(']')
        elif c == '{': stack.append('}')
        else:
            if c != stack[-1]: return value[c]
            else: stack.pop()
    #if stack == []: return ?
    return 0

score = 0
for line in data: score += parse_line(line)

print(score)
