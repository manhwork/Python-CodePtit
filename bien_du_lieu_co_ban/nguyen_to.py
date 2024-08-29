from math import *

def snt(n) :
    for i in range(2,isqrt(n)+1) :
        if n % i == 0 :
            return False
    return n > 1

def ntcn(n) :
    cnt = 0
    for i in range(1, n) :
        if gcd(i, n) == 1 :
            cnt+=1
    return snt(cnt)
    

t = int(input())

for _ in range(t):
    n = int(input())
    print( "YES" if ntcn(n) else "NO")

