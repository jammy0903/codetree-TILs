import sys 
from collections import deque
from itertools import permutations

for line in sys.stdin:
    s,n = line.split()
    n = int(n)
    word = list(s)
    total = len(word)
    if n > total:
        print(f"{s} {n} = No permutation")
        
        
    perm_list = list(permutations(s))
    print(perm_list[0])
     