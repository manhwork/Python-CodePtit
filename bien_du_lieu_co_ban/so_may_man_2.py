# PY01006
from math import *
t = int(input())

for _ in range(t):
    s = input()
    check = [x for x in s if (x != '4' and x != '7')]
    print("NO" if check else "YES")