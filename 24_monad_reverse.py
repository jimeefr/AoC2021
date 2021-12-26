#!/usr/bin/env python3

from common import *

data = read_input(24)
program = data

# On aurait pu utiliser un émulateur pour tester chaque valeur possible de chaque chiffre,
# en sauvegardant l'état des registres après chaque chiffre pour économiser, et traiter
# le problème de façon récursive... Mais la complexité et un peu trop grande.
#
# Un émulateur n'est donc pas utile pour la résolution, il faut faire du reverse!
#
# Le programme est constitué de 14 blocs presque identiques, aux valeurs Ai Bi et Ci près.
# (les Di sont les chiffres du code entré)
#  1 inp w      # w = Di
#  2 mul x 0    # x = 0
#  3 add x z    # x = z
#  4 mod x 26   # x = z % 26           -> x = Z[-1] = Dj+Cj
#  5 div z Ai   # z = z // Ai          -> si Ai == 26: Z.pop()
#  6 add x Bi   # x = Dj+Cj+Bi
#  7 eql x w    # si x == w : Une condition est à réaliser entre Di et un Dj précédent,
#  8 eql x 0    # x = !x      leur imposant une différence de Cj+Bi
#  9 mul y 0    # y = 0
# 10 add y 25   # y = 25
# 11 mul y x    # y = 0 ou 25
# 12 add y 1    # y = 1 ou 26
# 13 mul z y    # si la contition n'est pas réalisée:
# 14 mul y 0    # \
# 15 add y w    # |
# 16 add y Ci   # | z = z*26 + Di+Ci   -> Z.append(Di+Ci)
# 17 mul y x    # |
# 18 add z y    # /
# 
# La valeur des Ci est toujours positive mais jamais > 16. Donc 0 <= Ci+Di < 26
# Ai vaut soit 1 soit 26. Les opérations sur z se limitent à la division par 26, et
# la multiplication par 26 suivie d'un ajout d'un nombre < 26. On peut donc écrire z 
# comme la suite Z de ses chiffres en base 26, que l'on peut considérer comme une pile.
# z % 26 est le chiffre de poids faible, soit la dernière valeur empilée.
# z //= 26 correspond à un dépilement
# z = 26*z + X correspond à un empilement
#
# Le bloc est répété 14 fois. A chaque itération, une condition peut être réalisable
# entre le chiffre courrant et un chiffre précédemment empilé.
# Si Ai == 26, le chiffre alors utilisé est dépilé. Si on ne réalise pas la condition à
# cette itération, il restera des valeurs dans la pile Z, et z ne sera pas nul à la fin.
# 
# Si on réalise la condition à chaque fois que Ai==26 et que la condition n'est pas
# réalisable quand Ai==1, on finit en dépilant la dernière valeur de Z, et donc avec z=0.
# Si on a 7 itérations avec Ai==26 et une condition réalisable, et 7 itérations avec
# Ai==1 et une condition irréalisable, on a alors 7 conditions sur des paires de chiffre,
# et chaque chiffre apparait dans une condition et une seule.
# 
# Ces 7 conditions imposent des valeurs maximales et minimales sur chacun des chiffres.

M = [ ] # valeurs maximales des chiffres
m = [ ] # valeurs minimales des chiffres
A = [ ]
B = [ ]
C = [ ]
Z = [ (0,0) ] # A la première itération, il faut récupérer Cj=0. j n'a pas d'importance
              # car à cette itération, on doit avoir A=1, et une condition irréalisable
total = 1
for i in range(14):
    A.append(int(data[18*i + 4][6:]))
    B.append(int(data[18*i + 5][6:]))
    C.append(int(data[18*i +15][6:]))
    assert 0 <= C[i] < 26
    if i==0: assert A[i]==1
    m.append(1)
    M.append(9)
    j,Cj = Z[-1]
    delta = B[i]+Cj
    if A[i] == 26:
        assert i > 0
        assert -9 < delta < 9
        M[i] = min(9,9+delta)
        m[i] = max(1,1+delta)
        M[j] = min(9,9-delta)
        m[j] = max(1,1-delta)
        total *= 9-delta
        Z.pop()
    else:
        assert A[i] == 1
        assert abs(delta) >= 9
        Z.append((i,C[i]))
assert len(Z)==1
assert sum(A)==189 # 7*26 + 7*1
print("A :",A)
print("B :",B)
print("C :",C)
print("Plus grand code:", "".join(map(str,M)))
print("Plus petit code:", "".join(map(str,m)))
print("Nombre de codes possibles:", total)
