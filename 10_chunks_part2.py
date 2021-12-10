#!/usr/bin/env python3

from common import read_input

data = read_input(10)

def parse_line(line):
    stack=[]
    value = {')':1,']':2,'}':3,'>':4}
    for c in line:
        if c == '<': stack.append('>')
        elif c == '(': stack.append(')')
        elif c == '[': stack.append(']')
        elif c == '{': stack.append('}')
        else:
            if c != stack[-1]: return 0
            else: stack.pop()
    if stack == []: return 0
    s = 0
    for c in stack[::-1]: s = s * 5 + value[c]
    return s

scores = []
for line in data:
    s = parse_line(line)
    if s: scores.append(s)
scores.sort()

print(scores[len(scores)//2])
