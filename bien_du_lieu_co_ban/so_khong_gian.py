def check(s):
    for i in range(len(s) - 1) :
        if s[i] > s[i+1]: 
            return False
    return True

for t in range(int(input())) :
    s = input()
    print("YES" if check(s) else "NO")
