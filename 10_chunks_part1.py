#!/usr/bin/env python3

from common import read_input

data = read_input(10)

def parse_line(line):
    stack=[]
    value = {')':3,']':57,'}':1197,'>':25137}
    closing = {'(':')','[':']','{':'}','<':'>'}
    for c in line:
        if c in closing: stack.append(closing[c])
        elif c != stack[-1]: return value[c]
        else: stack.pop()
    return 0

print(sum(map(parse_line,data)))
