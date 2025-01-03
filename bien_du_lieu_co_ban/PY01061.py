from math import * 

def snt(n):
    for i in range(2,isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

if __name__ == "__main__" :
    for _ in range(int(input())):
        n = input()
        a = int(n[0:3])
        b = int(n[-3:])
        print("YES" if snt(a) and snt(b) else "NO")
    


# 3
# 12743
# 7337
# 12345678901234