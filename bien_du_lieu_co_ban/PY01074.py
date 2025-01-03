from math import *

def ptich(n):
    a = []
    for i in range(2,isqrt(n) + 1):
        if n % i ==0 :
            while n % i == 0 :
                a.append(i)
                n//=i 

    if n != 1 :
        a.append(n)

    return a


n = int(input())

result = []

for _ in range(n):
    n = int(input())
    result = [*result, *ptich(n)]

tong = 0 
for x in result : tong += x 
print(tong)

"""
5 
7
9 
10 
13 
100
"""