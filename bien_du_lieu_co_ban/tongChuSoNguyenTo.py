import math 
def snt(n):
    for i in range(2,math.isqrt(n)+ 1):
        if n % i ==0 :
            return False
    return n > 1

def check(n):
    tong = 0
    for x in n : 
        tong += int(x)
    return snt((tong))

for _ in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")

# 2
# 12341
# 22222222222222222222