from math import *

def snt(n):
    for i in range(2,isqrt(n) + 1):
        if n % i == 0 :
            return False
    return n > 1

def check(n):
    s = str(n)
    sum = 0
    for x in s : 
        sum += int(x)
    if snt(sum):
        return True
    else : 
        return False

for t in range(int(input())):
    a,b = map(int,input().split())
    print("YES" if check(gcd(a, b)) else "NO")


