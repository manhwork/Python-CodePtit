from math import *
def snt(n):
    for i in range(2,isqrt(n)+1):
        if n % i == 0 :
            return False
    return n > 1

def check(n):
    tong = 0
    for i in range(len(n)):
        tong += int(n[i])
        if i % 2 != 0 and int(n[i]) % 2 ==0:
            return False
        if i % 2 ==0 and int(n[i]) % 2 != 0:
            return False
    return snt(int(tong))


for _ in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")

# 2
# 2345678521
# 1212121212121212121212121
            
    