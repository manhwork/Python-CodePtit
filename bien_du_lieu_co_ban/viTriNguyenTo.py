from math import *
nto = ["2",'3','5','7']

def snt(n):
    for i in range(2,isqrt(n)+1):
        if n % i == 0 :
            return False
    return n > 1

def check(n):
    for i in range(len(n)):
        if snt(int(i)) and n[i] not in nto :
            return False
        if not snt(int(i)) and n[i] in nto : 
            return False
    return True

for _ in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")

# 2
# 14239567
# 2314514535353