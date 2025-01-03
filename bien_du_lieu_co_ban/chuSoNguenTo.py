from math import *
def snt(n):
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            return False
    return n > 1

def check(n):
    c1, c2 = 0, 0
    for x in n :
        if snt(int(x)):
            c1 +=1
        else :
            c2 += 1
    return c1 > c2 and snt(len(n))

def main():
    for _ in range(int(input())):
        n = input()
        print("YES" if check(n) else "NO")

main()

# 3
# 1234567
# 22334455667
# 23400300489898989