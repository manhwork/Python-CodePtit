def stn(n):
    if(len(n)==1) : 
        return False
    return n == n[::-1]

def tongCS(n):
    tong = 0
    for x in n :
        tong += int(x)
    return stn(str(tong))

for _ in range(int(input())):
    n = input()
    print("YES" if tongCS(n) else "NO")

# 2
# 12341
# 22222222222222222222