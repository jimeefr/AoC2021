#!/usr/bin/env python3

from common import *

data = read_input(24)
program = data

class alu():
    def load(self,prog):
        self.regs = {'x':0,'y':0,'z':0,'w':0}
        self.prog = prog
        self.ip = 0
        self.running = False
        self.input = []
    def p_inp(self,a):
        if self.input == []:
            self.running=False
            return
        self.regs[a] = self.input.pop(0)
    def value(self,b): return (self.regs[b] if b in "wxyz" else int(b))
    def p_add(self,a,b): self.regs[a] += b
    def p_mul(self,a,b): self.regs[a] *= b
    def p_div(self,a,b):
        assert b != 0
        self.regs[a] //= b
    def p_mod(self,a,b):
        assert self.regs[a] >= 0
        assert b > 0
        self.regs[a] %= b
    def p_eql(self,a,b):
        if self.regs[a] == b: self.regs[a]=1
        else: self.regs[a]=0
    def step(self):
        if self.ip >= len(self.prog):
            self.running = False
            return
        ins = self.prog[self.ip]
        token = ins.split()
        if token[0] == 'inp': self.p_inp(token[1])
        elif token[0] == 'add': self.p_add(token[1],self.value(token[2]))
        elif token[0] == 'mul': self.p_mul(token[1],self.value(token[2]))
        elif token[0] == 'div': self.p_div(token[1],self.value(token[2]))
        elif token[0] == 'mod': self.p_mod(token[1],self.value(token[2]))
        elif token[0] == 'eql': self.p_eql(token[1],self.value(token[2]))
        else: assert False,"Illegal instruction"
        if self.running: self.ip += 1
    def load_state(self,state): self.regs,self.ip = state
    def save(self): return self.regs,self.ip
    def run(self,inp,state=None):
        if state != None: self.load_state(state)
        self.input = inp
        self.resume()
    def resume(self):
        self.running = True
        while self.running:
            self.step()
    def valid(self): return self.regs['z']==0

def check(code):
    A = alu()
    A.load(program)
    A.run(code)
    return A.valid()

# On aurait pu utiliser l'émulateur pour tester chaque valeur possible de chaque chiffre,
# en sauvegardant l'état des registres après chaque chiffre pour accélérer, et traiter
# le problème de façon récursive... Mais la complexité et un peu trop grande.
# L'émulateur n'est donc pas utile pour la résolution, il faut faire du reverse!

M = 12996997829399
m = 11841231117189

print(M, check([ int(c) for c in str(M) ]))
print(m, check([ int(c) for c in str(m) ]))
