def check(n):
    n = str(n)
    if len(n) % 2 == 0:
        return False
    if n[0] == n[1]:
        return False
    for i in range(2,len(n),2):
        if n[i-2] != n[i]:
            return False
    return True 

for _ in range(int(input())):
    print("YES" if check(int(input())) else "NO")

# 2
# 2324272921262
# 13141516