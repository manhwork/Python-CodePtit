from math import * 

def isPrimeDigit(c) :
    if c == '2' or c == '3' or c == '5' or c == '7':
        return True
    return False

def snt(n):
    for i in range(2,isqrt(n) + 1):
        if n % i ==0 :
            return False
    return n > 1

def check(n):
    count = 0
    for c in n : 
        if(isPrimeDigit(c)):
            count += 1

    return snt(len(n)) and count > (len(n) - count)

if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        print("YES" if check(n) else "NO")


# 3
# 1234567
# 22334455667
# 23400300489898989